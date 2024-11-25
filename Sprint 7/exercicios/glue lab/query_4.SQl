SELECT ano, sexo, COUNT(nome) AS total_nomes
FROM frequencia_registro_nomes_eua
GROUP BY ano, sexo
ORDER BY ano DESC
LIMIT 10;