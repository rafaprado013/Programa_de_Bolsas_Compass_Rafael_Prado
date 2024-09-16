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
---

### Segue abaixo o script da normalização:

```SQL

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_localizacao

CREATE TABLE tb_localizacao (
    idLocalizacao INTEGER PRIMARY KEY AUTOINCREMENT,
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

INSERT OR REPLACE INTO tb_localizacao(cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao2;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_marcaCarro

CREATE TABLE tb_marcaCarro(
    idmarcaCarro INTEGER PRIMARY KEY AUTOINCREMENT,
    marcaCarro VARCHAR(40)
);

INSERT OR REPLACE INTO tb_marcaCarro(marcaCarro)
SELECT DISTINCT marcaCarro
FROM tb_locacao2;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_clientes

CREATE TABLE tb_clientes (
    idClientes INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(100),
    idLocalizacao VARCHAR(40),
    FOREIGN KEY (idLocalizacao) REFERENCES tb_localizacao(idLocalizacao)
);

INSERT OR REPLACE INTO tb_clientes(idClientes, nomeCliente, idLocalizacao)
SELECT idCliente, nomeCliente, idLocalizacao
FROM tb_locacao2 AS tbl2
LEFT JOIN tb_localizacao AS idl
    ON idl.cidadeCliente = tbl2.cidadeCliente;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_combustivel

CREATE TABLE tb_combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel TIME
);

INSERT OR REPLACE INTO tb_combustivel(idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao2;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_carros

CREATE TABLE tb_carros (
    idCarro INTEGER PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    idmarcaCarro INT,
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel),
    FOREIGN KEY (idmarcaCarro) REFERENCES tb_marcaCarro(idmarcaCarro)
);

INSERT OR REPLACE INTO tb_carros(idCarro, classiCarro, modeloCarro, anoCarro, kmCarro, idCombustivel, idmarcaCarro)
SELECT idCarro, classiCarro, modeloCarro, anoCarro, kmCarro, idCombustivel, tbmc.idmarcaCarro
FROM tb_locacao2 AS tbl2
RIGHT JOIN tb_marcaCarro AS tbmc
    ON tbmc.marcaCarro = tbl2.marcaCarro;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_vendedor

CREATE TABLE tb_vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

INSERT OR REPLACE INTO tb_vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao2;

-------------------------------------------------------------------------------------------------------------------------------------------------
-- Criação tb_locacao

CREATE TABLE tb_locacao (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18,2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES tb_clientes(idClientes),
    FOREIGN KEY (idCarro) REFERENCES tb_carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);

INSERT OR REPLACE INTO tb_locacao(idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao2;

-------------------------------------------------------------------------------------------------------------------------------------------------

DROP TABLE tb_locacao2 
````

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

### Segue abaixo o script da Dimensionalização:
``` SQL

SELECT * FROM tb_carros car;

SELECT * FROM tb_clientes cli;

SELECT * FROM tb_combustivel comb;

SELECT * FROM tb_localizacao;

SELECT * FROM tb_marcaCarro tmc 

SELECT * FROM tb_vendedor vend;

SELECT * FROM tb_locacao loc;

-- Criando o DW
   
-- Dimensão carros

create view dim_carros as
select  idCarro as id_carros,
		kmCarro as km_carro,
		classiCarro as classi_carro,
		marcaCarro as marca_carro,
		modeloCarro as modelo_carro,
		anoCarro as ano_carro,
		tbc.idCombustivel as id_combustivel,
		tipoCombustivel as tipo_combustivel
		
from tb_carros as car
left join tb_marcaCarro as tbmc
	ON tbmc.idmarcaCarro = car.idmarcaCarro
LEFT JOIN tb_combustivel AS tbc
	ON tbc.idCombustivel = car.idCombustivel

-- Dimensão clientes

create view dim_clientes as
select  idClientes as id_clientes,
        nomeCliente as nome_cliente,
        cidadeCliente as cidade_cliente,
        estadoCliente as estado_cliente,
        paisCliente as pais_cliente
   from tb_clientes AS cli
   LEFT JOIN tb_localizacao AS lcc
   	ON lcc.idLocalizacao = cli.idLocalizacao

-- Dimensão vendedor

create view dim_vendedor as
select  idVendedor as id_vendedor,
        nomeVendedor as nome_vendedor,
        sexoVendedor as sexo_vendedor,
        estadoVendedor as estado_vendedor
    from tb_vendedor vend;

-- Fato locacao

create view fato_locacao as
select  idLocacao  as id_locacao,
        idCliente as id_cliente,
        idCarro   as id_carro,
        idVendedor as id_vendedor,
        dataLocacao as data_locacao,
        horaLocacao as hora_locacao,
        qtdDiaria as qtd_diaria,
        vlrDiaria as vlr_diaria,
        dataEntrega as data_entrega,
        horaEntrega as hora_entrega
FROM tb_locacao AS tbloc;
LEFT JOIN tb_carros AS tbcar
	ON tbcar.idCarro = tbloc.id_Carro

	-- Dimensão tempo

CREATE VIEW dim_tempo AS
SELECT DISTINCT
    dataLocacao AS dataloc,
    substr(dataLocacao, 1, 4) AS ano,     
    substr(dataLocacao, 5, 2) AS mes,      
    substr(dataLocacao, 7, 2) AS dia       
FROM tb_locacao AS tbloc
WHERE dataLocacao IS NOT NULL;

-----------------------------------------------------------
-- Consultas ao DW

SELECT * FROM fato_locacao as fatoloc;  
   
SELECT * FROM dim_carros as dimcarros; 

SELECT * FROM dim_clientes as dimcli; 

SELECT * FROM dim_vendedor as dimvend; 

SELECT * FROM dim_tempo AS dimtempo;
```

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

