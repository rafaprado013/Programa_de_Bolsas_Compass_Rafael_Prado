# Etapas do desafio 1


### Etapa 1: Criação do diretório 'Ecommerce'

- Nesta etapa, através do comando *mkdir* foi realizada a criação do diretório 'Ecommerce', sendo o *sudo* para ganhar a permissão de administrador, e o ls para visualizar se foi realizada a criação efetiva do diretório.

![Passo 1: Criação do diretório Ecommerce](https://github.com/user-attachments/assets/5f584709-0086-443c-b2dd-6e406de89a45)

## 

 
### Etapa 2: Adicionando arquivo 'dados_de_vendas.csv'

- Nesta etapa foi necessário acessar o disco local do computador para copiar o **arquivo "dados_de_vendas.csv"** para o diretório Ecommerce através do comando *cp*

![Passo 2: Adicionando arquivo 'dados_de_vendas.csv'](https://github.com/user-attachments/assets/2ae3fd6c-0ba4-4363-b3ed-af0c46cdf919)

##

### Etapa 3: Criação do arquivo executável

- Aqui foi realiazada a crição do arquivo executavel com o editor de texto *nano* - a terminação **'sh'** se diz respeito ao arquivo executável.

![Etapa 3: Criação do arquivo executável](https://github.com/user-attachments/assets/c52eda65-9dc4-491e-87e9-3a6d0570e1d6)

##


### Etapa 4: Concedendo permissão para a execução do arquivo

- Nesta etapa do codigo foi dada a permissão ao usuário para executar este arquivo em específico. O *chmod* tem a utilidade de conceder mudanças de permissões, e o +x adiciona a permissão de EDITAR o arquivo citado imediatamente afrente.

![Etapa 4: Concedendo permissão para a execução do arquivo](https://github.com/user-attachments/assets/34d0602d-3de5-466c-9e22-a9807f033f71)

##

### Etapa 5: Criação do diretório 'vendas' e realização da copia do arquivo à pasta

- Estas são as primeiras ações do arquivo executavel, no caso, criar um diretório chamado **vendas**, e logo após copiar o arquivo **dados_de_vendas** presente no diretório 'ecommerce' para o dentro dele com o camando *cp*.

![Etapa 5: Criação do diretório 'vendas' e realização da copia do arquivo à pasta](https://github.com/user-attachments/assets/35de1683-03f9-4f4a-9451-5faa5011a0b0)

##

### Etapa 6: Criando subdiretório backup na pasta vendas e copiando o arquivo com a data atual no nome

- Aqui primeiro foi acessada a pasta vendas, para dentro dela ser criado o subdiretório **backup**. Na linha abaixo desta, foi criada uma variável chamada **data** (usando o $) a qual foi atribuida a data atual do sistema operacional no formato 'ANO, MÊS, DIA'.
-  Esta data é usada logo abaixo após copiarmos o arquivo 'dados_de_vendas.csv' para a pasta backup para enfim renomea-lo, usando a variável, dessa forma o arquivo terá a data atual acoplada ao nome sempre que for gerado.

![Etapa 6: Criando subdiretório backup na pasta vendas e copiando o arquivo com a data atual no nome](https://github.com/user-attachments/assets/5e832e07-8ad8-4946-b3d3-73f0a77bbbcd)

## 

### Etapa 7: Renomeando o arquivo

- Nesta fase é necessario novamente renomear o arquivo 'dados_de_vendas$data.csv' para '**backup**-dados-$data.csv', usando o comando *mv* para essa função, e por fim acessa-se a pasta **backup**.

![Etapa 7: Renomeando o arquivo](https://github.com/user-attachments/assets/f72c0134-900b-4c78-bdb0-465ffe72ef93)

##

### Etapa 8: Definindo variáveis para a exibição das datas no relatório

- Aqui definimos as variáveis que serão úteis para exibir a **data do sistema operacional**, **registro da primeira data**, **registro da ultima data** e a **quantidade de itens vendidos** no relatório.
- Primeiro é definida a variável **data_sistema_operacional', a qual guarda a data do sistema no formato ANO, MES, DIA, HORA, MINUTO'.
- Após isso é é definida a variável 'primeiro_registro_data', a qual exibe a data do primeiro registro do arquivo 'backup-dados-data.csv'. Segue os comandos usados e suas respectivas funções:
  - head -n 2 backup-dados-$data.csv: o *head* acessa as linhas do arquivo de cima para baixo, e o -n +2 indica que queremos a data da linha n° 2, pois na primeira encontra-se o cabeçalho.
  - cut -d ',' -f 5: o *cut -d ','* indica que estamos navegando entre as colunas com o separador ',', e o *f-5* indica que queremos a coluna 5.
 - Depois é definida a variável 'ultimo registro_data', a qual a função é semelhante a variável acima, sendo esta usada para guardar O ULTIMO registro. A unica mudança é no uso do comando *tail*, que interpreta o arquivo de baixo pra cima. Para ele é usado a flag -n 1, pois queremos a primeira linha de baixo pra cima (a ultima).
 - A proxima variável é 'qtd_itens_diferentes_vendidos', a qual retorna o numero de itens diferentes vendidos na tabela. Primero foi usado o *cut -d ',' -f2* para acessar a segunda coluna do arquivo, após isso foi usado o *tail -n 2* para acessar da ultima linha até a segunda; o *uniq* para remover duplicatas, e o *wc -l* para contar o numero de linhas.
- por fim foi definida a variável **relatório**, que guarda o nome 'relatório' com a data atual, assim a cada relatório gerado, o nome terá a data.
- A função dos echo's é exibir no relatório as informações guardadas dentro de cada variávvel citada, e as setas duplas (>>) para copiar a mensagem efetivamente no relatorio.


![Etapa 8: Definindo variáveis para a exibição das datas no relatório](https://github.com/user-attachments/assets/cf008e7d-6d41-4f46-8459-e6d7be064e30)

##

### Etapa 9: Exibindo as 10 primeiras linhas do arquivo de vendas no relatório

- Aqui usamos a função ja vista antes *head -n* para acessar as 10 primeiras linhas do arquivo citado afrente na imagem, e as setas duplas (>>) para replicar a mensagem no relatório, que é acessado em forma de variável ($).

![Etapa 9: Exibindo as 10 primeiras linhas do arquivo de vendas no relatório](https://github.com/user-attachments/assets/ff06cadc-5373-437f-84b9-bddfb6aa1006)

##

### Etapa 10: Compactando o arquivo em ZIP

Aqui foi feita a compactação do relatório para o formato ZIP pelo comando *zip -r*, na frente dele cita-se o nome final do arquivo e afrente o arquivo a ser compactado.

![Etapa 10: Compactando o arquivo em ZIP](https://github.com/user-attachments/assets/8161d8c6-1a1e-4ff6-8c03-a44d7861efd6)

##


### Etapa 11: Removendo o arquivo de vendas dos outros diretórios

- Para isso foi usado o comando *rm*, e afrente o arquivo a ser removido. O cat no fim servia para exibir o conteudo do relatório após ser executado, me ajudou no processo.

![Etapa 11: Removendo o arquivo de vendas dos outros diretórios](https://github.com/user-attachments/assets/d9da4038-e7e6-4347-ac12-3278318fcc01)

##

### Etapa 12: Executando o Crontab

- Para execução do crontab, foi utilizado o comando *crontab -e*, logo após, o cron é aberto no linux.

![Etapa 12: Executando o Crontab](https://github.com/user-attachments/assets/1ec59232-2b85-433d-bbad-cc5083a52c84)

## 

### Etapa 13: Agendando o horário de execução do arquivo executável

Para a execução é necessario passar ao cron os critérios desejados, podendo ser especificado a hora, minuto, dia do mes, mes e dia da semana. Os critérios devem ser especificados nesta respectiva ordem. Após as especificações, cita-se o endereço do arquivo executavel e seu nome. Asteriscos são usados quando os critérios não precisam ser especificados.


![Etapa 13: Agendando o horário de execução do arquivo executável](https://github.com/user-attachments/assets/7e5b4f00-3c86-40e4-b8c6-449aefe3d569)

##

### Etapa 14: Checando o funcionamento do Crontab
![Etapa 14 Checando o funcionamento do Crontab](https://github.com/user-attachments/assets/124c558c-9876-4b8b-a809-31751c9309e2)

- Para verificar o funcionamento do crontab é necessario usar o comando *sudo service cron status*, se mostrar o status 'active (running), escrito em verde, então está funcionando.

##

## Script do arquivo executável completo:
![arq_executavel_codigo](https://github.com/user-attachments/assets/e9263b19-3c07-4388-b829-23a79c516074)

##

# Execução do arquivo com o Crontab: Dia 1

- Aqui, observa-se que o cron executou o arquivo corretamente. As variáveis  estão sendo todas exibidas, a data do sistema operacional está atualizada, o numero de itens está correto, 10 itens estão sendo exibidos, e a compactação do arquivo de backup foi feita.

![Etapa 15: Execução do arquivo com o Crontab: Dia 1](https://github.com/user-attachments/assets/5207eac6-7e2d-4431-9449-4de6c12fe841)

##

# Execução do arquivo com o Crontab: Dia 2

- No dia de teste 2 foi acrescentada uma linha ao final do arquivo com novos dados. O relatório foi gerado com as devidas atualizações, diferindo do primeiro relatório na quantida de itens vendidos, data do ultimo registro e nome do relatório. Outra cópia do backup foi feita e outro relatorio foi gerado devidamente.
 
![Execução do arquivo com o Crontab: Dia 2](https://github.com/user-attachments/assets/6378eac3-ecbb-491a-90d3-fd2985ec3488)

##

# Execução do arquivo com o Crontab: Dia 3

- No dia de teste 3, como nos outros demais, foi gerado um novo relatorio com a data atual e uma nova copia do arquivo de backup. Foi novamente acrescrentada uma nova linha ao final do arquivo, logo, o numero de itens vendidos aumentou em um. A data também atualizou, assim como o nome do arquivo e a data do ultimo registro.


![Execução do arquivo com o Crontab: Dia 3](https://github.com/user-attachments/assets/a2ff0d2e-19bc-4c31-a675-20c82746a528)

##

# Execução do arquivo com o Crontab: Dia 4

- No dia de teste 4, assim como nos demais dias, a execução ocorreu perfeitamente, alterando as variáveis (foi adicionada novamente uma nova linha no arquivo csv, como nos outros dias).

![Execução do arquivo com o Crontab: Dia 4](https://github.com/user-attachments/assets/f96f4811-af6e-477a-9748-e1d7a9ca4e74)

##

## Criação do arquivo executavel "Consolidador de processamento de vendas"

- Neste passo, foi criado o arquivo executável 'consolidador_de_processamento_de_vendas.sh' com nano.

![Criacção do arquivo "consolidador de processamento de vendas"](https://github.com/user-attachments/assets/bee656f7-5434-4a8f-b623-23f61e150701)

##

# Script do consolidador

- Nesta etapa foi feito o script do consolidador. Para isso foi necessário acessar o diretório 'vendas' e depois 'backup', para enfim ser criado o arquivo "relatorio_final.txt". O comando *cat >>* foi usado para exibir a mensagem de cada relatório em particular dentro do arquivo relatorio_final.txt, e também por questão de estética foi criada uma variável chamada 'pontilhado', a qual junto ao 'echo' exibe um traço no relatório apenas para separar os relatórios um do outro e otimizar a visualização.

![passo_16_script_consolidador_de_processamento_de_vendas](https://github.com/user-attachments/assets/15b0802b-08a7-424e-b6fd-4d2c7988b002)

##

# Execucao do consolidador

-Aqui foi feita a execução do consolidador atraves do comando './' e foi verificado através do comando *tree* que a execução ocorreu perfeitamente, sendo assim o arquivo 'relatorio_final.txt' criado dentro do diretório 'backup'.

![passo_17_execucao_consolidador_de_processamento_de_vendas](https://github.com/user-attachments/assets/cb342b8a-b77a-44d5-ad1d-caf8d91ce920)

##

# Leitura do relatório final

- Por fim, nota-se que o relatóriio final foi executado corretamente, exibindo as informações dos quatro relatórios gerados ao longo dos dias. 

![passo_18_leitura_relatorio_final](https://github.com/user-attachments/assets/710ea44e-6925-4746-ac2c-05bbd7ba3fad)

