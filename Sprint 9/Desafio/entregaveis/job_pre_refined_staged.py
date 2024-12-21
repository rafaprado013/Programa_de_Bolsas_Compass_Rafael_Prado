import sys
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from awsglue.dynamicframe import DynamicFrame

# Inicializando contextos Glue e Spark
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Declarando caminhos de entrada
caminho_s3_entrada1 = "s3://data-lake-do-rafael-prado/Trusted/JSON/2024/12/13/"
caminho_s3_entrada2 = "s3://data-lake-do-rafael-prado/Trusted/CSV/2024/12/12/"

# Lendo dados da Trusted em DynamicFrame e convertendo em Dataframe
dados_json = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3",
    connection_options = {"paths": [caminho_s3_entrada1]},
    format = "parquet"
).toDF()

# Lendo dados do CSV em DynamicFrame e convertendo em Dataframe
dados_csv = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3",
    connection_options = {"paths": [caminho_s3_entrada2]},
    format = "parquet"
).toDF()

# Renomeando a coluna "generoArtista" para inglês
dados_csv = dados_csv.withColumnRenamed("generoArtista", "artist_genre")

# Realizando a junção, mantendo os dados do JSON e incluindo algumas colunas do CSV
dados_juntos = dados_json.join(dados_csv, dados_json["title"] == dados_csv["tituloPincipal"], "inner") \
                         .select(dados_json["*"], dados_csv["artist_genre"])

# Agrupando colunas com a coluna "artist_genre" em forma de lista
dados_agrupados = dados_juntos.groupBy(
    "id", "title", "original_title", "release_date", "runtime",
    "vote_count", "vote_average", "revenue", "original_language",
    "genres", 'origin_country', 'adult', 'budget', 'popularity'
).agg(
    F.collect_set("artist_genre").alias("artist_genre")
)

# Convertendo 'artist_genre' de array para string
dados_agrupados = dados_agrupados.withColumn("artist_genre", F.concat_ws(", ", F.col("artist_genre")))

# Convertendo de volta para DynamicFrame
dynamic_frame_agrupado = DynamicFrame.fromDF(dados_agrupados, glueContext, "dynamic_frame_agrupado")

data_atual = datetime.now()
ano = data_atual.strftime("%Y")
mes = data_atual.strftime("%m")
dia = data_atual.strftime("%d")
caminho_s3_saida = f"s3://data-lake-do-rafael-prado/pre-refined/{ano}/{mes}/{dia}/"

# Salvando dados na pré-refined (staged)
glueContext.write_dynamic_frame.from_options(
    frame = dynamic_frame_agrupado,
    connection_type = "s3",
    connection_options = {"path": caminho_s3_saida},
    format = "parquet"
)

job.commit()
