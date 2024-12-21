import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import explode, split, trim, col, row_number, year, month, dayofmonth, regexp_replace
from pyspark.sql.window import Window

# Inicializando o contexto Glue e Spark
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos de entrada e saída
input_path = "s3://data-lake-do-rafael-prado/pre-refined/2024/12/13/"
output_path = "s3://data-lake-do-rafael-prado/Refined/"

# Lendo o arquivo Parquet em um DynamicFrame
datasource0 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [input_path], "recurse": True},
    transformation_ctx="datasource0"
)
 
# Conversão para DataFrame para manipulação
df = datasource0.toDF()

# Dimensão Filme
dim_filme = df.select('id', 'title', 'original_title', 'runtime', 'original_language', 'adult', 'revenue', 'budget')

# Dimensão Tempo
dim_tempo = df.select('release_date').distinct()
dim_tempo = dim_tempo.withColumn("ano", year(col("release_date"))) \
    .withColumn("mes", month(col("release_date"))) \
    .withColumn("dia", dayofmonth(col("release_date")))
windowSpecTempo = Window.orderBy("release_date")
dim_tempo = dim_tempo.withColumn("id_tempo", row_number().over(windowSpecTempo))

# removendo colchetes da coluna origin_country
df = df.withColumn("origin_country", trim(regexp_replace(col("origin_country"), "\\[|\\]", "")))

# Dimensão Localização
dim_localizacao = df.select(explode(split(col("origin_country"), ",")).alias("localizacao")).distinct()
dim_localizacao = dim_localizacao.withColumn("localizacao", trim(col("localizacao")))
windowSpecLocalizacao = Window.orderBy("localizacao")
dim_localizacao = dim_localizacao.withColumn("id_localizacao", row_number().over(windowSpecLocalizacao))
dim_localizacao = dim_localizacao.dropDuplicates(["localizacao"])
dim_localizacao = dim_localizacao.filter(col("localizacao") != "")

# Separando siglas da coluna localizacao
df = df.withColumn("localizacao", explode(split(trim(regexp_replace(col("origin_country"), "\\[|\\]", "")), ",")))

# Criação da Tabela Fato Filme
fato_filme = df.select('id', 'release_date', 'vote_count', 'vote_average', 'popularity', 'localizacao')
fato_filme = fato_filme \
    .join(dim_filme.select('id', col('id').alias('id_filme')), on='id') \
    .join(dim_tempo.select('release_date', 'id_tempo'), on='release_date', how='left') \
    .join(dim_localizacao.select('localizacao', 'id_localizacao'), on='localizacao', how='left')

# Conversão de DataFrame para DynamicFrame para salvar no Glue
dim_filme_dyf = DynamicFrame.fromDF(dim_filme, glueContext, "dim_filme_dyf")
dim_tempo_dyf = DynamicFrame.fromDF(dim_tempo, glueContext, "dim_tempo_dyf")
dim_localizacao_dyf = DynamicFrame.fromDF(dim_localizacao, glueContext, "dim_localizacao_dyf")
fato_filme_dyf = DynamicFrame.fromDF(fato_filme, glueContext, "fato_filme_dyf")

# Salvando as tabelas dimensionais e de fatos no S3
glueContext.write_dynamic_frame.from_options(
    dim_filme_dyf, 
    connection_type="s3", 
    connection_options={"path": f"{output_path}dim_filme/"}, 
    format="parquet"
)
glueContext.write_dynamic_frame.from_options(
    dim_tempo_dyf, 
    connection_type="s3", 
    connection_options={"path": f"{output_path}dim_tempo/"}, 
    format="parquet"
)
glueContext.write_dynamic_frame.from_options(
    dim_localizacao_dyf, 
    connection_type="s3", 
    connection_options={"path": f"{output_path}dim_localizacao/"}, 
    format="parquet"
)
glueContext.write_dynamic_frame.from_options(
    fato_filme_dyf, 
    connection_type="s3", 
    connection_options={"path": f"{output_path}fato_filme/"}, 
    format="parquet"
)

job.commit()
