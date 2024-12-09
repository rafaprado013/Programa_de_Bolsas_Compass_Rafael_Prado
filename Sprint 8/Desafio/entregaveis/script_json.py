import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, udf, to_date, when, expr
from pyspark.sql.types import ArrayType, StringType


args = getResolvedOptions(sys.argv, ['Job Json'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['Job Json'], args)

caminho_origem = "s3://data-lake-do-rafael-prado/Raw/TMDB/JSON/2024/11/28/"

# Lendo os arquivos JSON em um DynamicFrame:
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_origem]},
    format="json"
)

# Transformando o DynamicFrame em um DataFrame:
data_frame = dynamic_frame.toDF()

# Função para extrair apenas os nomes dos gêneros:
def extrair_nomes_dos_generos(generos):
    return [genero['name'] for genero in generos]

# Registrando a função como um UDF (User Defined Function):
extrair_nomes_dos_generos_udf = udf(extrair_nomes_dos_generos, ArrayType(StringType()))

# Aplicando a função UDF à coluna "genres" para extrair apenas os nomes:
data_frame = data_frame.withColumn("genres", extrair_nomes_dos_generos_udf(col("genres")))

# Convertendo a coluna release_date para o formato de data
data_frame = data_frame.withColumn("release_date", to_date(data_frame["release_date"], "yyyy-MM-dd"))

# Colunas a manter nos arquivos:
colunas_manter = ["id", "title", "original_title", "release_date", "runtime", "vote_count", "vote_average", "revenue", "original_language"]
data_frame_filtrado = data_frame.select(*colunas_manter)

# Removendo dados nulos e linhas sem title ou original_title:
data_frame_limpo = data_frame_filtrado.dropna(subset=["title", "original_title"])
data_frame_limpo = data_frame_limpo.filter(data_frame_limpo.title.isNotNull() & data_frame_limpo.original_title.isNotNull())

# Removendo duplicatas
data_frame_limpo = data_frame_limpo.dropDuplicates(colunas_manter)

# Corrigindo a coluna revenue para conter apenas valores inteiros:
data_frame_limpo = data_frame_limpo.withColumn("revenue", col("revenue.int").cast("int"))
data_frame_limpo = data_frame_limpo.withColumn("revenue", when(col("revenue") == 0, None).otherwise(col("revenue")))

# Convertendo a coluna runtime para valores inteiros:
data_frame_limpo = data_frame_limpo.withColumn("runtime", col("runtime").cast("int"))

# Garantindo que vote_count e vote_average sejam números válidos:
data_frame_limpo = data_frame_limpo.withColumn("vote_count", col("vote_count").cast("int"))
data_frame_limpo = data_frame_limpo.withColumn("vote_average", col("vote_average").cast("float"))

# Convertendo o DataFrame limpo de volta para DynamicFrame
dynamic_frame_transformado = DynamicFrame.fromDF(data_frame_limpo, glueContext, "dynamic_frame_transformado")

# Definindo o caminho de destino para os arquivos PARQUET:
data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')
caminho_destino = f"s3://data-lake-do-rafael-prado/Trusted/JSON/{ano}/{mes}/{dia}/"

# Escrevendo o DynamicFrame transformado no formato PARQUET:
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_transformado,
    connection_type="s3",
    connection_options={"path": caminho_destino},
    format="parquet"
)

job.commit()
