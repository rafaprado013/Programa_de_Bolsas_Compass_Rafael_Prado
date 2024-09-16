# Etapas do Desafio 2

### Etapa 1: Normalização

- Nesta etapa, a normalização foi feita através da criação de tabelas, com o intuito de deixar cada tipo de dado em uma tabela, pois na tabela locação na sua forma bruta (que foi renomeada como tb_locacao2) haviam informações sobre varios 'objetos' em uma só tabela. E para a realização da normalização, a tb_locacao2 foi repartida nas seguintes tabelas:
     - tb_localização
     - tb_marcaCarro
     - tb_clientes
     - tb_combustivel
     - tb_carros
     - tb_vendedor
     - tb_locacao

Cada uma com suas devidas informações dentro de si.

![01_normalizacao_parte_1](https://github.com/user-attachments/assets/e13cc0cd-4527-4d23-befd-8a67f024dade)

![01_normalizacao_parte_2](https://github.com/user-attachments/assets/ecda6dcf-fd55-427d-827b-ceb9f2f3e305)

![01_normalizacao_parte_3](https://github.com/user-attachments/assets/1bb246cd-1d5a-451c-97eb-00a64eb93280)

---

Abaixo encontra-se o passo a passo usado para criação das tabelas. A titulo de exemplificação, usarei a criação da tabela tb_locacao:
#
  1. CRIANDO A TABELA COM O CREATE TABLE - comando usado para criar cada tabela vazia.
     
     ![criando_tabela](https://github.com/user-attachments/assets/5b2d0364-9cb8-41db-9064-7e1440b067dd)

  2. ESCOLHA DO NOME DAS COLUNAS - logo após o comando CREATE TABLE deve se nomear as colunas da tabela.
   
![image](https://github.com/user-attachments/assets/00bcf77e-5141-4b80-853c-9d9aa960b4a7)

  3. ADIÇÃO DA CHAVE PRIMARIA PELO COMANDO *INTEGER PRIMARY KEY* - fazendo isso, estamos dando uma chave primária a alguma coluna da tabela.

  ![image](https://github.com/user-attachments/assets/0310f341-963b-4e6a-8f9d-94a991154c7a)

  - obs: em algumas tabelas foi necessario usar o comando AUTOINCREMENT (tb_lolcalizacao // tb_marcaCarro) para a geração automatica de numeros ordenados nas colunas que receberam a chave primária da tabela. O comando encontra-se imediatamente afrente do comando "INTEGER PRIMARY KEY"

![image](https://github.com/user-attachments/assets/6da8e481-66a2-440f-8efe-fbbcadf78860)


  4. SELEÇÃO DO TIPO DA COLUNA - Nessa parte, selecionamos o formato da coluna. Os formatos usados variam de acordo com a coluna - os formatos usados foram: varchar, int, smalint, time, date, datetime.
     
  ![image](https://github.com/user-attachments/assets/e97446b1-0518-4952-825c-3698bd156662)

  5. ADIÇÃO DA *FOREIGN KEY* - é o comando que faz a conexão e entre duas tabelas.
      
![image](https://github.com/user-attachments/assets/d8d52af3-37b1-4e87-8d1d-6659b09037fa)

 
  6. INSERT OR REPLACE INTO - Esse comando foi usado para adicionar à nova tabela criada informações de colunas selecionadas da tb_locacao2 (tabela original com todas as informações).
  
 ![image](https://github.com/user-attachments/assets/f134014a-29d2-4898-996f-ba7ea197e606)

  7. SELECT - no comando select, selecionamos as o nome das colunas que precisamos da tb_locacao2
      
![image](https://github.com/user-attachments/assets/c3cab022-08bb-444e-9794-cfeb5efd97a0)

  8. FROM - no comando *from*, selecionamos o nome da tabela que queremos pegar a informação - No caso, tb_locacao2

![image](https://github.com/user-attachments/assets/afe98aaa-2c08-497c-8920-c862eae40811)


   9. LEFT JOIN - esse comando é foi usado para exibir em uma tabela informações contidas em outra tabela atráves de duas informações emc comum.
      obs: esse comando não foi usado na criação da tb_locacao, então, a titulo de exemplo será usado a criação da tabela "tb_carros"

![image](https://github.com/user-attachments/assets/e6bcfd48-8463-4977-8661-2706fef70d55)

##### O PROCESSO ACIMA FOI REPETIDO PARA AS 7 TABELAS CITADAS NO INICIO DESTE README.

#

Após a ciração das tabelas, esse foi o resultado no banco de dados DBeaver:

![02_criacao_tabelas](https://github.com/user-attachments/assets/7fded523-9fa2-4396-9004-ee2c8c04b335)

O resultado via diagrama foi o seguinte:

![diagrama_modelagem_relacional](https://github.com/user-attachments/assets/835fa188-a175-45e2-a3ec-a0a33b0cd2bb)

O diagrama foi feito atrávés do site dbdiagram.io

##

### Etapa 2: Dimensionalização

- Na dimensionalização foi preciso desfazer parte do processo anterior, ou seja, "desnormalizar" para obter o reusltado desejado. Para isso, foi feita a criação de VIEWS, e no processo, e foi necessario juntar algumas das tabelas criadas anteriormente e criar uma nova, que seria uma tabela de TEMPO, chamada "dim_tempo" (dimensão tempo). Cada VIEW é um DIMENSÃO, e também foi criada a tabela fato, chamada "fato_locacao". As dimensões criadas foram as seguintes.
     - dim_carros
     - dim_clientes
     - tb_clientes
     - dim_tempo
--- 

Segue abaixo o Script para a criação das dimensões:

  ![03_dimensionalizacao_parte_1](https://github.com/user-attachments/assets/94eb05dc-909e-49a8-9f55-343b2788d830)
  
![03_dimensionalizacao_parte_2](https://github.com/user-attachments/assets/029b1bed-1484-45e3-afe6-5a265898339c)

A criação das 4 dimensões tambem seguiu determinado padrão. A título de exemplo será usada criação da dimensão "fato_locacao" O passo a passo utilzado foi o descrito abaixo:

1. SELEÇÃO DAS TABELAS - o primeiro passo foi a seleção das tabelas as quais nos baseariamos para criar as dimensões.

![image](https://github.com/user-attachments/assets/5a908f40-2708-46bb-aef4-f24f9c6e66be)

2. CREATE VIEW AS - para criar uma view foi usado o comando CREATE VIEW AS, como se segue na imagem abaixo:

![image](https://github.com/user-attachments/assets/dde4067c-8f03-4490-8cf2-81a1a7778e4d)


3. SELECT DO NOME DAS COLUNAS - nessa parte citamos as colunas que queremos extrair da tabela normalizada que escolhermos, e logo afrente usamos o AS para renomerar cada coluna selecionada.
   
![image](https://github.com/user-attachments/assets/9c18bc86-189a-4769-b08a-203bf317cca8)

4. SELEÇÃO DA TABELA NORMALIZADA - aqui declaramos a tabela da qual extrairemos os dados.

   ![image](https://github.com/user-attachments/assets/c3addf9e-f226-44da-8511-b5059072799d)

5. EXTRAINDO COLUNAS DE OUTRAS TABELAS - nessa fase, se necessario extrair colunas de outras tabelas, usamos o left join.

![image](https://github.com/user-attachments/assets/edededcd-5c2a-46ad-bdb7-76d622c93369)

---

A unica exeção na forma de criação foi a tabela tempo.

![image](https://github.com/user-attachments/assets/40e25991-4007-434d-8c5d-4d1d86774937)

Para a criação dela, foi necessario usar o SELECT DISTINCT, para que não hajam informações repetidas na tabela. Tambem foi usado o comando *substr* para recortar da data que estava no formato "yyyymmaa" os numeros num outro formato. Fazendo isso, o resultado é a coluna ano no formato YYYY, mês no formato MM, e dia no formato dd.

---

O resultado após a execução dos codigos foi o abaixo:

![04_criacao_views_dimensionalizacao](https://github.com/user-attachments/assets/23e5d719-2997-485e-a7d4-20ad6ca3be1a)

---

Em seguida, verifica-se o diagrama do modelo dimensional criado:

![diagrama_modelagem_dimensional](https://github.com/user-attachments/assets/82f52f9d-5865-4213-b71b-78850da5cb4c)

---

### MÉTRICAS

Ao final do desafio, foram criadas por mim duas métricas, com o objetivo de demonstrar a performace do modelo dimensional, e como pode ser eficaz para consultas.

#### MÉTRICA 1: Gasto por cliente

  #### SCRIPT:

![selecao_metricas_gasto_cliente](https://github.com/user-attachments/assets/be1d54d7-8555-4de0-abeb-1de312b94a01)

Para a criação do script acima foi feita a seleção dos clientes de uma forma que eles não se repetissem na exibição, usando um SELECT DISTINCT. Tambem foi criada uma coluna do lucro de cada cliente, multiplicando as colunas qtdDiaria e vlrDiaria. Após isso foi feito a conexão da tabela tb_locacao com a tabela dim_clientes através do left join, com o objetivo de poder consultar a coluna "nome_cliente". Por fim, foi feito o agrupamento por nome do cliente, com a ordenação por valor do lucro, do maior pro menor, usando o comando DESC.

#### RESULTADO:

![selecao_metrica_resultado_gasto_cliente](https://github.com/user-attachments/assets/fb39d1c2-77d2-49c8-9ee4-cde78d8f9832)

### Métrica 2: Gasto por estado

  #### SCRIPT:

![selecao_metricas_lucro_estado](https://github.com/user-attachments/assets/b9d81400-5a83-48eb-a0d8-30662a666f6a)

Para a criação do script acima foi feita a seleção dos estados de uma forma que eles não se repetissem na exibição, usando também o comando SELECT DISTINCT. Após isso foi criada uma coluna do do lucro total por estado, multiplicando as colunas qtdDiaria e vlrDiaria. Após isso foi feito a conexão da tabela tb_locacao com a tabela dim_clientes através do left join, com o objetivo de poder consultar a coluna "estado_cliente". Finalmente, foi feito o agrupamento por estado do cliente, sendo a exibição em ordem alfabética.

#### RESULTADO:

![selecao_metrica_resultado_lucro_estado](https://github.com/user-attachments/assets/6ec4bc97-0663-4e06-9fb0-501e409176f5)

