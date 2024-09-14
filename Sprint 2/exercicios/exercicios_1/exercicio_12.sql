select cddep, nmdep, dtnasc, sum(vrunt * qtd) as valor_total_vendas
from tbdependente tbd
left join tbvendas as tbv
	on tbv.cdvdd = tbd.cdvdd
left join tbvendedor as tbvdd
	on tbvdd.cdvdd = tbd.cdvdd
where tbv.cdvdd = 9 and tbv.status = 'Concluído'
group by (tbv.cdvdd)