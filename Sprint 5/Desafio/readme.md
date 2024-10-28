## Sobre o CSV escolhido:

- O tema da base de dados escolhida através do site "dados.gov.br" foi "Obitos confirmados por covid 19 em Minas Gerais" desde o ano de 2024, tendo sido feita a ultima atualização da base de dados em janeiro/2024. Esse foi o tema escolhido porque é considerado não só pro mim um tema relevante, visto que foi um virus que teve impacto global.

---

## ETAPA 1:



-  O propósito da etapa 1 é criar um espaço de armazenamento na nuvem (um bucket no S3 da AWS) e fazer o upload de um arquivo local, chamado obitos-confirmados-covid-19.csv, para esse espaço. Isso prepara o terreno para guardar e acessar esse arquivo de forma centralizada e segura na nuvem, o que facilita o compartilhamento e a manipulação dos dados depois.
- Segue abaixo a evidência do código e em seguida o passo a passo feito para sua devida execução:

![Evidencia_criacao_bucket](../../Sprint%205/evidencias/00_codigo_criacao_upload_bucket.png)

1. **Conexão com o S3**: Primeiramente, a biblioteca `boto3` é importada para interação com a AWS, especificamente com o S3.
2. **Criação do cliente e do bucket**:
   - O cliente S3 é criado usando `boto3.resource('s3')`.
   - O nome do bucket é definido na variável `bucket`.
   - O comando `s3.create_bucket(Bucket=bucket)` cria o bucket no S3 com o nome especificado.
3. **Upload do arquivo**:
   - A variável `arquivo` define o caminho do arquivo local a ser enviado ao S3.
   - O arquivo é renomeado no bucket para `nome_arquivo` e, em seguida, é feito o upload usando `s3.Bucket(bucket).upload_file(arquivo, nome_arquivo)`.
4. **Confirmação**: Uma mensagem é exibida confirmando o upload com sucesso.

---


## Confirmação da devida execução do código no terminal:

![01_1_upload_csv_bucket](../../Sprint%205/evidencias/01_1_upload_csv_bucket.png)

## Evidência da criação do bucket na AWS:

![01_criacao_bucket_desafio](../../Sprint%205/evidencias/01_criacao_bucket_desafio.png)

## Evidência do upload do CSV no bucket criado:

![02_upload_csv_bruto_bucket](../../Sprint%205/evidencias/02_upload_csv_bruto_bucket.png)

---

## ETAPA 2:

- O codigo da etapa 2 é responsável por baixar o arquivo obitos-confirmados-covid-19.csv do bucket no S3, carregar os dados para análise e realizar várias transformações úteis. Ele filtra pacientes homens acima de 60 anos, agrupa dados por município, adiciona uma coluna para indicar presença de comorbidades e ajusta outros detalhes, como o formato da idade, data do óbito e capitalização dos nomes dos municípios. Depois dessas modificações, ele salva e reenvia três arquivos com os dados processados de volta ao bucket no S3, criando versões filtradas, agrupadas e completas do dataset.
- Segue abaixo a evidência do código e em seguida o passo a passo feito para sua devida execução:

![03_codigo_upload_csvs](../../Sprint%205/evidencias/03_codigo_upload_csvs.png)


1. **Leitura do arquivo do S3**: Um cliente S3 é criado com `boto3.client('s3')`, e o arquivo `obitos-confirmados-covid-19.csv` é baixado, sendo transformado em um DataFrame usando `pd.read_csv`.
2. **Funções de transformação**:
   - **Filtrar pacientes masculinos com idade > 60**: A função `filtrar_pacientes_masculinos_mais_60` retorna um DataFrame com pacientes masculinos acima de 60 anos.
   - **Agrupamento por município**: `agregar_pacientes_por_municipio` agrupa pacientes por município através do groupby, contando total de pacientes e idade média.
   - **Coluna de comorbidade**: A função `adicionar_coluna_comorbidade` adiciona a coluna `TEM_COMORBIDADE`, indicando a presença de comorbidade com "Sim" ou "Não".
   - **Conversões de dados**:
     - **Idade para inteiro**: `converter_idade_para_inteiro` converte os valores da coluna `IDADE` para inteiros.
     - **Extração do ano de óbito**: `converter_data_obito_e_extrair_ano` transforma `DATA_OBITO` em datetime e extrai o ano.
     - **Maiúsculas para municípios**: `transformar_municipios_maiusculas` altera `MUNICIPIO_RESIDENCIA` para maiúsculas.
3. **Salvando os resultados no S3**: Os DataFrames resultantes são salvos em buffers CSV e enviados de volta ao S3 com os nomes `df_filtrado.csv`, `df_agg.csv` e `df_completo.csv`.

---

### Abaixo encontram-se as evidências de exibição das queries:


![04_1_df_final_atualizado](../../Sprint%205/evidencias/04_1_df_final_atualizado.png)

![04_2_pacientes_acima_60_y](../../Sprint%205/evidencias/04_2_pacientes_acima_60_y.png)

![04_3_pacientes_agregacao_por_municipio](../../Sprint%205/evidencias/04_3_pacientes_agregacao_por_municipio.png)

---

### Segue abaixo a evidência do upload dos 3 CSV'S dentro do bucket:


![evidencia_upload_csvs_finais](../../Sprint%205/evidencias/evidencia_upload_csvs_finais.png)

---

### E por fim, a evidência da base de dados inicial, sem tratamentos:


![04_0_40_primeiras_linhas_df_bruto](../../Sprint%205/evidencias/04_0_40_primeiras_linhas_df_bruto.png)

#
