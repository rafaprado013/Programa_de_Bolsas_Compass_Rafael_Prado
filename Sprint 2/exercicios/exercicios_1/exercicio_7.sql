with sem_pub as (
select
    nome,
    count(lvr.cod) as quantidade
from autor atr
left join livro lvr on atr.codautor = lvr.autor
group by atr.nome
having quantidade = 0
)

select nome
from sem_pub