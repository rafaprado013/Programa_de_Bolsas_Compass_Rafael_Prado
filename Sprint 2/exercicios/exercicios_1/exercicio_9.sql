with most_s_p as (
select cdpro, nmpro, sum(qtd) as qtd
from tbvendas
where (dtven between '2014-02-03 00:00:00' and '2018-02-02 00:00:00') and (status = 'Concluído')
group by cdpro
order by qtd desc
limit 1
)

select cdpro, nmpro
from most_s_p