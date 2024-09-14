select cdcli, nmcli, sum(vrunt * qtd) as gasto
from tbvendas
group by cdcli 
order by gasto desc
limit 1