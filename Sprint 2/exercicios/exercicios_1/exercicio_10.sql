select
    tvd.nmvdd as vendedor,
    sum(tbv.qtd * tbv.vrunt) as valor_total_vendas,
    round(sum(tbv.qtd * tbv.vrunt) * tvd.perccomissao / 100, 2) as comissao
from tbvendas tbv
join tbvendedor as tvd
    on tbv.cdvdd = tvd.cdvdd
where tbv.status = 'Concluído'
group by tvd.nmvdd
order by comissao desc;