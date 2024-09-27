### ETAPA 1:
- O primeiro passo dado rumo ao desafio, foi a importação das bibliotecas Pandas e Matpotlib, apelidando as como *pd* e *plt*.

![Passo_1_importando_bibliotecas](https://github.com/user-attachments/assets/7d77f824-6899-44cf-9d9b-4fc8930620a9)

- E logo após, foi feita a leitura do arquivo, da forma que se segue:

![Passo_2_lendo_o_arquivo](https://github.com/user-attachments/assets/a00af826-7b28-444a-81ba-5d6b5b7e39c9)

---

### ETAPA 2:
- Na criação do grafico de barras (Top 5 apps por número de instalações), primeiro foi feita a eliminação de linhas duplicadas e de dados duplicados na coluna "App", e a exclusão de uma linha fora do padrão
  que estava dando erro na filtragem (linha n° 10472). No código abaixo também é feito o tratamento da coluna 'Installs", removendo caracteres inadequados e a transformando em uma coluna numérica, pois estava em formato 'objeto'.
  E por ultimo, é feito a filtragem das 5 primeiras linhas das colunas App e Installs, organizadas por valores do maior para o menor.
- Após isso, é feita a plotagem do grafico pela biblioteca Matplotlib (plt) - Usando os comandos abaixo, a partir do "plt.figure()"

![Passo_3_criando_exibindo_grafico](https://github.com/user-attachments/assets/6d4ed073-b1a9-4d38-9d08-421483ae86f8)

---

### ETAPA 3:
- Na etapa 3 é feita a criação do grafico de pizza por categorias de apps do dataset por frequência. Para isso, primeiro é feita a contagem do número de categorias na coluna 'Category', calculado seu total e enfim o valor é
transformado em porcentagem. As porcentagens abaixo de 2,4 são somadas e transformadas na "fatia" chamada "Outros", em verde, enquanto as porcentagens maiores que este valor são exibidas normalmente como fatias individuais.
- Após isso, é feita a plotagem do gráfico.

![Passo_4_criando_exibindo_grafico_pizza](https://github.com/user-attachments/assets/12b8b801-2eb2-4ab4-b376-f3b73b9aa888)

---

### ETAPA 4:
- Nesta etapa foi feita a consulta do app mais caro do Dataset. Para isso, tive que pegar o mesmo tratamento da coluna "Installs" que fiz anteriormente e colocar no mesmo bloco do código, pois sem ele, apenas executando anteriormente,
estava dando erro. Após isso, a coluna "Price" também foi tratada removendo caracteres desnecessarios, e seu formato foi mudado para numérico assim como a coluna Installs.
Por fim, é feita a seleção das colunas "App" e "Price", organizadas por valores do maior pro menor, e selecionada apenas a primeira linha, ou seja, com maior valor, **pelo critério "Price".** Abaixo do código encontra-se o resultado.

![Passo_5_consulta_app_mais_caro](https://github.com/user-attachments/assets/5ec95912-c9e8-449c-b484-b0aed14e4d94)

---

### ETAPA 5:
- Nesta etapa, foi realizada a contagem de apps com classificação "Mature 17+" no dataset. Para isso, utilizou-se uma query que filtra as linhas onde a coluna "Content Rating" possui o valor "Mature 17+", retornando
as colunas "App" e "Content Rating". Em seguida, os dados foram agrupados pela coluna "App" e ordenados alfabeticamente para facilitar a visualização. Por fim, o número total de apps classificados como "Mature 17+"
foi exibido numa mensagem com base no número de linhas resultantes.

![Passo_6_consulta_num_app_mature17](https://github.com/user-attachments/assets/3ce95e20-3c84-43a6-a930-d5386cc0ec6c)

---

### ETAPA 6:
- Nesta etapa é feita a consulta do Top 10 Apps por número de reviews. Para essa consulta é feito a alteração do formato da coluna "Reviews" para numérico, após isso são selecionadas as colunas "App" e "Reviews",
   organizadas pela coluna Reviews do maior para o menor, exibindo as 10 primeiras linhas, o que corresponde aos 10 apps com mais reviews.

![Passo_7_consulta_top10_app_review](https://github.com/user-attachments/assets/56b21c6a-d322-44e3-94b9-95c7a7432347)

---

### ETAPA 7:
- Nesta etapa foi realizada a consulta dos apps mais caros por categoria. Para isso, primeiramente, foi feito o tratamento da coluna Price, removendo o caractere $ e convertendo-a para numérico. Em seguida, foi realizado o agrupamento por Category para encontrar o preço máximo de cada uma. Utilizando o método
  idxmax(), foi possível identificar o índice do app mais caro por categoria. Após isso, foram selecionadas as colunas App, Category e Price e ordenadas de forma decrescente com base na coluna Price. Por fim, o resultado foi exibido, contendo os apps mais caros por categoria do dataset.

![Passo_8_consulta_apps_mais_caros_categ](https://github.com/user-attachments/assets/df95b417-bab7-4122-af88-7416a5d69ce6)

---

### ETAPA 8:
- Nesta etapa, foi realizada a consulta dos apps com maior número de Reviews da categoria Medicina. Para isso, primeiro, foi feita a filtragem dos aplicativos que possuem a palavra 'Medical' na coluna Genres. Em seguida, tratou-se a coluna Reviews, convertendo-a para numérico, já que estava em formato 'objeto'.
Depois disso, foi feita a seleção do app com o maior número de Reviews utilizando o método idxmax(). O resultado foi exibido, mostrando o app com maior número de Reviews da categoria Medicina.

![Passo_9_consulta_app_maior_n_review](https://github.com/user-attachments/assets/56236044-11e4-4dd9-9f03-fe32bd2bfacc)

---


### ETAPA 9:
- Nesta etapa foi feito um histograma da distribuição das avaliação da categoria GAME. Para isso, foi feita uma filtragem, selecionando as linhas em que na coluna "category" em que o texto fosse igual a "GAME". E logo após, essa fitlragem foi plotada e exibida em grafico de acordo com frequencia das notas.

![Passo_10_histograma](https://github.com/user-attachments/assets/728d1829-e672-4c82-a59a-a249959e097a)

---

### ETAPA 10:
Aqui foi feito um grafico de dispersão entre instalções e avaliações. Para fazer isso, foi necessário novamente repetir o processo de limpeza da coluna install ja feito anteriormente, caso contrário, dava erro; tambem foi feita a transformação da coluna "rating" para formato numérico. Após isso foram eliminados da tabela os registros que estavam como "NA", e por fim foi plotado o grafico, sendo o mesmo exibido na tela.

![Passo_11_dispersao](https://github.com/user-attachments/assets/3c9791b7-48c9-43c3-95d5-362a3c3b6faf)


