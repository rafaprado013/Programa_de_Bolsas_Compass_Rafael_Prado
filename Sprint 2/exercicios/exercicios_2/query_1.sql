select 
	lvr.cod as CodLivro,
	lvr.titulo as Titulo,
	lvr.autor as Autor,
	atr.nome as NomeAutor,
	lvr.valor as Valor,
	lvr.editora as CodEditora,
	edt.nome as NomeEditora
from
	livro as lvr
left join
	autor as atr
		on atr.codautor = lvr.autor 
left join
	editora as edt
		on edt.codeditora = lvr.editora
order by
	valor desc
limit 10
