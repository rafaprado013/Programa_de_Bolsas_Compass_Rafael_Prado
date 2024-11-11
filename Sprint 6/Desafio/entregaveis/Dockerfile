#Usando a imagem do Python 3.9 como base
FROM python:3.9

#Definindo o diretório de trabalho a ser usado no container
WORKDIR /app

#Definindo o volume
VOLUME ["/app/volume"]

#Copiando o script e os arquivos CSV para o volume do container
COPY script.py /app/volume/script.py
COPY series.csv /app/volume/series.csv 
COPY movies.csv /app/volume/movies.csv

#Instalando a biblioteca boto3
RUN pip install boto3

#Executa o script python
CMD ["python", "/app/volume/script.py"]
