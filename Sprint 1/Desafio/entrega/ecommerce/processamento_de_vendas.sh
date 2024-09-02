mkdir vendas
cp ecommerce/dados_de_vendas.csv vendas/
cd vendas/
mkdir backup/
data=$(date +'%Y%m%d')
cp dados_de_vendas.csv backup/dados-vendas-$data.csv
mv backup/dados-vendas-$data.csv backup-dados-$data.csv
mv backup-dados-$data.csv backup
cd backup
data_sistema_operacional=$(date +'%Y%m%d %HH:%MM')
primeiro_registro_data=$(head -n 2 backup-dados-$data.csv | cut -d ',' -f 5)
ultimo_registro_data=$(tail -n 1 backup-dados-$data.csv | cut -d ',' -f 5)
qtd_itens_diferentes_vendidos=$(cut -d',' -f2 backup-dados-$data.csv | tail -n +2 | uniq | wc -l)
relatorio="relatorio-$data.txt"
echo 'Data do sistema operacional: '$data_sistema_operacional >> "$relatorio"
echo 'Data do primeiro registro: '$primeiro_registro_data >> "$relatorio"
echo 'Data do ultimo registro: '$ultimo_registro_data >> "$relatorio"
echo 'Quantidade total de itens diferentes vendidos: '$qtd_itens_diferentes_vendidos >> "$relatorio"
head -n 10 backup-dados-$data.csv >> "$relatorio"
zip -r backup-dados-$data.zip backup-dados-$data.csv
rm backup-dados-$data.csv
cd ..
rm dados_de_vendas.csv
cat backup/"$relatorio"
