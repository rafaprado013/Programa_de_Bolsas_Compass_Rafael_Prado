select distinct atr.nome
from livro
left join editora as edt
	on edt.codeditora = livro.editora
left join endereco as edr		
	on edr.codendereco = edt.endereco
left join autor as atr
	on atr.codautor = livro.autor
where edr.estado <> 'PARANÁ' and edr.estado <> 'SANTA CATARINA' and edr.estado <> 'RIO GRANDE DO SUL'
order by atr.nome