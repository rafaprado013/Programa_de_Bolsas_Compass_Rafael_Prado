select tbvn.estado, tbvn.nmpro, round(avg(tbvn.qtd), 4) as quantidade_media
from tbvendas as tbvn
where tbvn.status = 'Concluído'
group by tbvn.estado, tbvn.nmpro
order by tbvn.estado asc, tbvn.nmpro asc