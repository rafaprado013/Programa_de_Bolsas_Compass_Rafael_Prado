select 
	lvr.editora as CodEditora,
	edt.nome as NomeEditora,
	count (cod) as QuantidadeLivros
from
	livro as lvr
left join
	editora as edt
		on edt.codeditora = lvr.editora
group by edt.nome

