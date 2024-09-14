select tbvn.estado, 
       round(avg((tbvn.vrunt) * (tbvn.qtd)), 2) as gastomedio
from tbvendas as tbvn
where tbvn.status = 'Concluído'
group by tbvn.estado
order by gastomedio desc