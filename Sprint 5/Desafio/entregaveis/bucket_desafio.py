import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')
nome_bucket = 'desafio-sprint05-bucket'
nome_arquivo = 'obitos-confirmados-covid-19.csv'

baixar_arquivo = s3.get_object(Bucket=nome_bucket, Key=nome_arquivo)
arquivo = baixar_arquivo['Body'].read().decode('utf-8')

df = pd.read_csv(StringIO(arquivo), sep=';')


def filtrar_pacientes_masculinos_mais_60(df):
    return df[(df['SEXO'] == 'M') & (df['IDADE'] > 60)]


def agregar_pacientes_por_municipio(df):
    return df.groupby('MUNICIPIO_RESIDENCIA').agg(
        total_pacientes=('PACIENTE', 'count'),
        idade_media=('IDADE', 'mean')
    ).reset_index()


def adicionar_coluna_comorbidade(df):
    df['TEM_COMORBIDADE'] = df['COMORBIDADE'].apply(
        lambda x: 'Sim' if pd.notna(x) else 'Não')
    return df


def converter_idade_para_inteiro(df):
    df['IDADE'] = df['IDADE'].astype(int)
    return df


def converter_data_obito_e_extrair_ano(df):
    df['DATA_OBITO'] = pd.to_datetime(df['DATA_OBITO'], errors='coerce')
    df['ANO_OBITO'] = df['DATA_OBITO'].dt.year
    return df


def transformar_municipios_maiusculas(df):
    df['MUNICIPIO_RESIDENCIA'] = df['MUNICIPIO_RESIDENCIA'].str.upper()
    return df


df_filtrado = filtrar_pacientes_masculinos_mais_60(df)
df_agg = agregar_pacientes_por_municipio(df)
df = adicionar_coluna_comorbidade(df)
df = converter_idade_para_inteiro(df)
df = converter_data_obito_e_extrair_ano(df)
df = transformar_municipios_maiusculas(df)

# Exibindo os resultados
print("Filtro de Pacientes do Sexo Masculino e Idade > 60")
print(df_filtrado.head(40))

print("\nAgregação de Pacientes por Município")
print(df_agg.head(40))

print("\nDataFrame Atualizado")
print(df.head(40))

buffer_filtered = StringIO()
buffer_agg = StringIO()
buffer_df = StringIO()

df_filtrado.to_csv(buffer_filtered, index=False)
df_agg.to_csv(buffer_agg, index=False)
df.to_csv(buffer_df, index=False)

# Enviando os CSVs para o S3
s3.put_object(Bucket=nome_bucket, Key='df_filtrado.csv',
              Body=buffer_filtered.getvalue())
s3.put_object(Bucket=nome_bucket, Key='df_agg.csv', Body=buffer_agg.getvalue())
s3.put_object(Bucket=nome_bucket, Key='df_completo.csv',
              Body=buffer_df.getvalue())

print("Arquivos enviados com sucesso para o bucket")
