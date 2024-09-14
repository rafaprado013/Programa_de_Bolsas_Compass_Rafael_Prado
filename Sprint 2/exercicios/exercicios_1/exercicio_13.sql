select tbvn.cdpro, tbvn.nmcanalvendas, tbvn.nmpro, sum(tbvn.qtd) as quantidade_vendas
from tbvendas as tbvn
left join tbestoqueproduto as tbpr
	on tbpr.cdpro = tbvn.cdpro
where tbvn.status = 'Concluído' and (tbvn.nmcanalvendas = 'Ecommerce' or tbvn.nmcanalvendas = 'Matriz')
group by tbvn.cdpro, tbvn.nmcanalvendas, tbvn.nmpro
order by quantidade_vendas asc
limit 10