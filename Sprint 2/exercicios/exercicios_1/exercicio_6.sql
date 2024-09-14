select atr.codautor, atr.nome, count(autor) as quantidade_publicacoes
from livro as lvr
left join autor as atr
	on atr.codautor = lvr.autor
group by autor
order by quantidade_publicacoes desc
limit 1