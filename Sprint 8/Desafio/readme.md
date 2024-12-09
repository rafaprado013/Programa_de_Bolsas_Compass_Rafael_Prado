## Neste desafio foram feitos 2 scripts para tratar dois diferentes formatos de arquivos, sendo o primeiro em CSV, e o segundo em JSON. Os processos são de certa forma semelhantes, e em virtude disso, serão explicados de forma paralela nas etapas.

# ETAPA 1

O propósito dos códigos abaixo é realizar uma série de tarefas para `processar e limpar dados armazenados em arquivos CSV'S e JSON no S3`, utilizando as ferramentas `AWS Glue` e `PySpark`, e enfim salvando-os em um bucket no formato `Parquet`.

### SCRIPT USADO NO JOB DO CSV:
- Segue abaixo o ``script  usado para a realização do processamento, limpeza, e transformação dos dados do CSV para Parquet`` (`ETL`), com sua devida expicação através dos comentários:

```python

import sys
from pyspark.context import SparkContext 
# Cria um contexto Spark (entrada para toda a funcionalidade do Spark). Coordena a execução de operações de transformação e ação em dados distribuídos;
from awsglue.context import GlueContext
# cria um contexto que permite a interação com o AWS Glu;
from awsglue.dynamicframe import DynamicFrame
# Permite a manipulação de dados de um modo mais flexível;
from pyspark.sql.functions import lit
# Fornece várias funções para manipular dados em DataFrames do Spark;
from awsglue.job import Job
#Importa a classe Job, usada para criar, inicializar e gerenciar Jobs no AWS Glue;
from awsglue.utils import getResolvedOptions
# Usado para obter e resolver opções de execução passadas como argumentos na linha de comando ao iniciar o trabalho do Glue;
from datetime import datetime

#Declarando camino do arquivo CSV a ser tratado
source_file = "s3://data-lake-do-rafael-prado/Raw/Local/CSV/Movies/2024/11/11/movies.csv"

# Inicializando o GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("MoviesJob", {})

# Lendo o arquivo CSV no S3 com delimitador pipe "|"
df = spark.read.option("delimiter", "|").csv(source_file, header=True, inferSchema=True)

# Verificando o esquema do DataFrame
df.printSchema()

# Removendo as colunas desnecessárias
df_tratado = df.drop("titulosMaisConhecidos", "profissao", "anoFalecimento", "anoNascimento", "nomeArtista", "personagem")

# removendo os dados nulos e linhas duplicadas
df_tratado = df_tratado.dropna().dropDuplicates()

if df_tratado.count() == 0:
    raise ValueError("Nenhum dado disponível para salvar no destino.")

# Convertendo o DataFrame de volta para DynamicFrame
dynamic_frame_tratado = DynamicFrame.fromDF(df_tratado, glueContext)

data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')

target_path = f"s3://data-lake-do-rafael-prado/Trusted/CSV/{ano}/{mes}/{dia}/"

# Salvando os dados no S3 em formato Parquet
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_tratado,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)

job.commit()


```
--- 

### SCRIPT USADO NO JOB DO JSON:
- Segue abaixo o ``script  usado para a realização do processamento, limpeza, e transformação dos dados do JSON para Parquet``, com sua devida expicação através dos comentários:

```python

import sys
from datetime import datetime
from awsglue.transforms import * 
# Importa todas as transformações disponíveis no AWS Glue para manipulação e transformação de dados;
from awsglue.utils import getResolvedOptions  
# Usado para obter e resolver opções de execução passadas como argumentos na linha de comando ao iniciar o trabalho do Glue;
from pyspark.context import SparkContext
# Importa a classe SparkContext, essencial para criar o contexto Spark, que coordena a execução de operações de transformação e ação em dados distribuídos;
from awsglue.context import GlueContext
# cria um contexto que permite a interação com o AWS Glu;
from awsglue.job import Job
# Importa a classe Job, usada para criar, inicializar e gerenciar Jobs no AWS Glue;
from awsglue.dynamicframe import DynamicFrame
# Permite a manipulação de dados de um modo mais flexível;
from pyspark.sql.functions import col, udf, to_date, when, expr
# Importa várias funções do módulo pyspark.sql.functions, usadas para manipulação de colunas e definição de funções definidas pelo usuário (UDF);
from pyspark.sql.types import ArrayType, StringType
# Importa tipos de dados do PySpark, como ArrayType e StringType, usados para definir esquemas de dados.



# Inicializando o Glue e o job:
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#Declarando o caminho do arquivo JSON a ser tratado
source_path = "s3://data-lake-do-rafael-prado/Raw/TMDB/JSON/2024/11/28/"

# Lendo os arquivos JSON em um DynamicFrame:
dynamic_frame_tratado = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_path]},
    format="json"
)

# Transformando o DynamicFrame em um dataframe:
data_frame = dynamic_frame_tratado.toDF()

# Função para extrair apenas os nomes dos gêneros:
def extrair_nomes_dos_generos(genres):
    return [genre['name'] for genre in genres]

# Registrando a função como um UDF (User Defined Function):
extrair_nomes_dos_generos_udf = udf(extrair_nomes_dos_generos, ArrayType(StringType()))

# Aplicando a função UDF à coluna "genres" para extrair apenas os nomes:
data_frame = data_frame.withColumn("genres", extrair_nomes_dos_generos_udf(col("genres")))

# Convertendo a coluna release_date para o formato de data (estava como string)
data_frame = data_frame.withColumn("release_date", to_date(data_frame["release_date"], "yyyy-MM-dd"))

# Colunas que decidi manter nos arquivos:
colunas_manter = ["id", "title", "original_title", "release_date", "runtime", "vote_count", "vote_average", "revenue", "original_language"]
filtered_data_frame = data_frame.select(*colunas_manter)

# Removendo dados nulos e linhas sem title ou original_title:
data_frame_tratado = filtered_data_frame.dropna(subset=["title", "original_title"])
data_frame_tratado = data_frame_tratado.filter(data_frame_tratado.title.isNotNull() & data_frame_tratado.original_title.isNotNull())

# Removendo duplicatas
data_frame_tratado = data_frame_tratado.dropDuplicates(colunas_manter)

# Corrigindo a coluna revenue para conter apenas valores inteiros:
data_frame_tratado = data_frame_tratado.withColumn("revenue", col("revenue.int").cast("int"))
data_frame_tratado = data_frame_tratado.withColumn("revenue", when(col("revenue") == 0, None).otherwise(col("revenue")))

# Convertendo a coluna runtime para valores inteiros:
data_frame_tratado = data_frame_tratado.withColumn("runtime", col("runtime").cast("int"))

# Garantindo que vote_count e vote_average sejam números válidos
data_frame_tratado = data_frame_tratado.withColumn("vote_count", col("vote_count").cast("int"))
data_frame_tratado = data_frame_tratado.withColumn("vote_average", col("vote_average").cast("float"))

# Convertendo o DataFrame limpo de volta para DynamicFrame
dynamic_frame_tratado_transformado = DynamicFrame.fromDF(data_frame_tratado, glueContext, "dynamic_frame_tratado_transformado")

# Definindo o caminho de destino para os arquivos Parquet:
data_atual = datetime.now()
ano = data_atual.strftime('%Y')
mes = data_atual.strftime('%m')
dia = data_atual.strftime('%d')
target_path = f"s3://data-lake-do-rafael-prado/Trusted/JSON/{ano}/{mes}/{dia}/"

# Escrevendo o DynamicFrame transformado no formato Parquet:
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_tratado_transformado,
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)


job.commit()

```

# ETAPA 2

- Na etapa 2 foi feita a ``execução dos jobs do CSV e do JSON``. Segue a baixo as devidas evidencias de execução corretas:

### Run JOB CSV: 

![x](./..//evidencias/Parquet%20CSV/03_run_job.png)


### Run JOB JSON: 

![x](./..//evidencias/Parquet%20JSON/03_run_job.png)

---

- Em seguida foi feita a confirmação de que os ``CSVs e JSONs foram transformados em Parquets em suas devidas pastas dentro do bucket no AWS S3``:

### Confirmação da transformação do CSV em Parquet:
![x](./..//evidencias/Parquet%20CSV/pos_execucao_job_csv.png)

### Confirmação da transformação do JSON em Parquet:
![x](./..//evidencias/Parquet%20JSON/04_pos_execucao_json.png)

# ETAPA 3

Nesta etapa foi feita a ``criação do Database`` no qual serão armazenadas as tables criadas pelos ``crawlers``. Foi usado o mesmo database tanto para a table do CSV quanto do JSON.

![x](./..//evidencias/Parquet%20JSON/database_usado.png)


# ETAPA 4

- Na etapa 4 foi feita de forma respectiva a ``criação dos Crawlers``, suas ``execuções`` e a ``verificação da criação das tables`` após a execução dos crawlers. segue abaixo as evidências:

### DO CSV:

#### Crawler CSV:
![x](./..//evidencias/Parquet%20CSV/05_crawler_csv.png)

#### Execução do Crawler CSV: 
![x](./..//evidencias/Parquet%20CSV/06_execucao_crawler.png)

#### Criação da table CSV:

![x](./..//evidencias/Parquet%20JSON/tables.png)


### DO JSON:

#### Crawler JSON:
![x](./..//evidencias/Parquet%20JSON/05_crawler_json.png)

#### Execução do Crawler JSON: 
![x](./..//evidencias/Parquet%20JSON/execucao_crawler_json.png)

- obs: foram feitas diversas execuções, até conseguir o resultado esperado.

#### Criação da table CSV:
![x](./..//evidencias/Parquet%20JSON/tables.png)

# ETAPA 5

- Aqui foram realizadas as ``queries para consulta das tables no AWS Athena`` com objetivo de verificar tudo que foi feito no codigo foi efetivamente aplicado. Foram executadas diversas queries, mas para o propósito do desafio será mostrada apenas uma query mais básica.

### Query do Parquet do CSV:

![x](./..//evidencias/Parquet%20CSV/07_query_athena.png)

#### Schema CSV:

![x](./..//evidencias/Parquet%20CSV/08_schema_csv.png)

---


### Query do Parquet do JSON:

![x](./..//evidencias/Parquet%20JSON/06_query_athena.png)

#### Schema JSON:

![x](./..//evidencias/Parquet%20JSON/schema.png)

### Questões / Analises a serem feitas:

- Relação entre `filmes com notas médias altas` (notaMedia) e `(numeroVotos)`/ comparação com filmes medianos. Exemplo: Filmes mais bem avaliados tem mais ou menos votos que filmes mal avaliados? 
- `relação do numero de filmes de Ação` em que o protagonista é do `genero mascuino/feminino`, com o intuito de comparar a discrepância entre o numero de atrizes / atores em filmes de Ação;
- `Evolução do faturamento dos filmes 'Ação/Aventura' ao longo das 5 ultimas decadas décadas.`
