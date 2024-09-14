---- CONCESSIONARIA

-- Consultas
-- --------


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