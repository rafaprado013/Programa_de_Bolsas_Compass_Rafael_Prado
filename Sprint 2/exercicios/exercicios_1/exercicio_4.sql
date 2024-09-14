select
    nome,
	codautor,
	nascimento,
	count(cod) as quantidade
from autor atr
left join livro lvr on atr.codautor = lvr.autor
group by nome
order by nome asc 

