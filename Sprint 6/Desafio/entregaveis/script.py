import boto3
from datetime import datetime

# Definindo nomes dos arquivos e o bucket
arquivo_filmes = '/app/movies.csv'
arquivo_series = '/app/series.csv'
bucket = 'data-lake-do-rafael-prado'
camada = 'Raw'
origem = 'Local'
formato = 'CSV'
especificacao_filmes = 'Movies'
especificacao_series = 'Series'

# Data atual para o caminho
data_processamento = datetime.now().strftime('%Y/%m/%d')

# Inicializando o cliente do S3
s3 = boto3.client('s3')

# Função para enviar arquivos para o S3
def enviar_para_s3(arquivo_local, especificacao, arquivo_nome):
    caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_processamento}/{arquivo_nome}"
    s3.upload_file(arquivo_local, bucket, caminho_s3)
    print(f"Arquivo '{arquivo_nome}' enviado para o S3 em: {caminho_s3}")


# Enviando os arquivos
enviar_para_s3(arquivo_filmes, especificacao_filmes, 'movies.csv')
enviar_para_s3(arquivo_series, especificacao_series, 'series.csv')
