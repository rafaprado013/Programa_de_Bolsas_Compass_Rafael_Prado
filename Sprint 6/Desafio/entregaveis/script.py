import boto3
from datetime import datetime

#Definindo os caminhos locais dos arquivos CSV de filmes e séries
arquivo_filmes = '/app/movies.csv'
arquivo_series = '/app/series.csv'

#Nome do bucket S3 onde os arquivos serão armazenados
bucket = 'data-lake-do-rafael-prado'

#Definindo a estrutura da pasta no S3
camada = 'Raw'        
origem = 'Local'        
formato = 'CSV'            
especificacao_filmes = 'Movies'  
especificacao_series = 'Series'  
data_processamento = datetime.now().strftime('%Y/%m/%d')

#Inicializando o cliente S3 com boto3
s3 = boto3.client('s3')

#Função para enviar um arquivo local para o S3
def enviar_para_s3(arquivo_local, especificacao, arquivo_nome):
    caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_processamento}/{arquivo_nome}"
    s3.upload_file(arquivo_local, bucket, caminho_s3)
    print(f"Arquivo '{arquivo_nome}' enviado para o S3 em: {caminho_s3}")


#Executando a função e enviando arquivos para o s3
enviar_para_s3(arquivo_filmes, especificacao_filmes, 'movies.csv')
enviar_para_s3(arquivo_series, especificacao_series, 'series.csv')  
