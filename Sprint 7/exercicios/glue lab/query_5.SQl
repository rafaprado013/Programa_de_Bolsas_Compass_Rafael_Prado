SELECT nome, ano, total
FROM frequencia_registro_nomes_eua
WHERE sexo = 'F'
ORDER BY total DESC
LIMIT 1;