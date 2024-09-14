select nome, cidade, estado, count(*) as quantidade
from livro as lvr
left join editora as edt
	on lvr.editora = edt.codeditora
left join endereco as edr
	on edt.endereco = edr.codendereco
group by(nome)select nome, cidade, estado, count(*) as quantidade
from livro as lvr
left join editora as edt
	on lvr.editora = edt.codeditora
left join endereco as edr
	on edt.endereco = edr.codendereco
group by(nome)