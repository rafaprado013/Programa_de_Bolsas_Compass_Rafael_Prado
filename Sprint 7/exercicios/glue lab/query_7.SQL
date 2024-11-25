SELECT ano, SUM(CAST(total AS BIGINT)) AS total_registros
FROM frequencia_registro_nomes_eua
GROUP BY ano
ORDER BY ano ASC
LIMIT 10;
