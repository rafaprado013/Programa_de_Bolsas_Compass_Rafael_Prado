# Use a imagem oficial do Python
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script Python para o container
COPY script.py .
COPY series.csv .
COPY movies.csv .

# Instala boto3 para integração com o S3
RUN pip install boto3

# Comando para executar o script Python
CMD ["python", "script.py"]
