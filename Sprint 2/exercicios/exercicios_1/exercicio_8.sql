with best_sm as (
select vdr.cdvdd, cdven, nmvdd, sum(qtd) as qtd
from tbvendas
left join tbvendedor as vdr
	on vdr.cdvdd = tbvendas.cdvdd
where status = 'Concluído'
group by vdr.cdvdd
order by qtd desc
limit 1
)

select cdvdd, nmvdd
from best_sm