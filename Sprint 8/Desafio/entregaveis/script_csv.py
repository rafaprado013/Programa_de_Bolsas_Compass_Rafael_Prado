import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import lit
from awsglue.job import Job
from datetime import datetime


arquivo_origem = "s3://data-lake-do-rafael-prado/Raw/Local/CSV/Movies/2024/11/11/movies.csv"

# Inicializando o contexto do Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("MoviesJob", {})

# Lendo o arquivo CSV no S3 com delimitador pipe "|"
df = spark.read.option("delimiter", "|").csv(arquivo_origem, header=True, inferSchema=True)

# Removendo as colunas desnecessárias
df_limpo = df.drop("titulosMaisConhecidos", "profissao", "anoFalecimento", "anoNascimento", "nomeArtista", "personagem")

# Limpando os dados
df_limpo = df_limpo.dropna().dropDuplicates()

# Convertendo o DataFrame de volta para DynamicFrame
dynamic_frame_limpo = DynamicFrame.fromDF(df_limpo, glueContext, "dynamic_frame_limpo")

data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')

caminho_destino = f"s3://data-lake-do-rafael-prado/Trusted/CSV/{ano}/{mes}/{dia}/"

# Salvando os dados no S3 em formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_limpo,
    connection_type="s3",
    connection_options={"path": caminho_destino},
    format="parquet"
)

job.commit()

print("Dados processados e salvos com sucesso no S3!")
