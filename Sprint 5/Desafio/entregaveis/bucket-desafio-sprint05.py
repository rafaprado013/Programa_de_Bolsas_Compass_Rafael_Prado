import boto3

# criação do cliente S3
s3 = boto3. resource('s3')

# declarando nome do bucket
bucket = 'desafio-sprint05-bucket'

# criando o bucket
s3.create_bucket(Bucket=bucket)

# caminho do arquivo
arquivo = "C:/Users/Rafael/Desktop/PB_Compasso_UOL/Sprint 5/Desafio/entregaveis/obitos-confirmados-covid-19.csv"

# Nome do arquivo no bucket
nome_arquivo = 'obitos-confirmados-covid-19.csv'

# Fazendo upload do arquivo para o bucket
s3.Bucket(bucket) .upload_file(arquivo, nome_arquivo)

print(f'Arquivo {nome_arquivo}\ enviado para o bucket {bucket} com sucesso!')
