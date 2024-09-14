
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
