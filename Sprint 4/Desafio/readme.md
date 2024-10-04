## ETAPA 1:

- Segue abaixo a explicação dos codigos e a evidência do código usado para definir como a imagem será construída:


- Primeiro, a linha *FROM python:3.12.7-slim* define a imagem base do Docker. Em seguida, *WORKDIR /app* estabelece que o diretório de trabalho dentro do container será /app, garantindo que todos os comandos seguintes sejam executados nesse diretório. O comando *COPY carguru.py .* copia o arquivo carguru.py do sistema local para o diretório */app* dentro do container. Por fim, *CMD ["python", "carguru.py"]* define o comando a ser executado quando o container for iniciado, que é rodar o arquivo carguru.py utilizando o Python.

![alt text](image-1.png)

---

#### Abaixo, segue-se a evidência da criação da imagem:

![alt text](image-2.png)


---

#### Após isso, foi feita a execução do container - abaixo segue-se seu resultado:

![alt text](image-3.png)

#

## ETAPA 2:

#### Na etapa dois foi necessário responder as seguintes perguntas: 

![alt text](image.png)


- Respondendo a primeira pergunta: Sim, pode-se reutiliza-lo e pode ser reiniciado sem a necessidade de cria-lo novamente. Reinicia-se através do comando: *docker start*

#

## ETAPA 3:

- #### Na imagem abaixo é definida a forma como a imagem do script python será construída:

![alt text](image-4.png)

- obs: os comandos usados para isso foram os mesmos da etapa 1, a alteração feita foi apenas a mudança do nome "carguru" para "script", por ser outra imagem.

#

#### Abaixo, encontra-se a explicação dos comandos e da evidência do algoritmo que recebe uma string, gerando o Hash por meio do algoritmo SH4, e que por fim exibe a Hash em tela usando o método *hexdigest*.

- Primeiramente, o módulo *hashlib* é importado para permitir o uso de funções de hash, como SHA-1. Em seguida, um loop infinito *while True* é utilizado para que o programa continue pedindo entradas indefinidamente. O programa solicita ao usuário que digite uma string com *input()* e essa string é transformada em um *hash SHA-1* usando *hashlib.sha1()*, que converte a string em bytes com *.encode()* e, finalmente, gera a representação em hexadecimal com *hexdigest()*. Por fim, o valor do hash gerado é exibido com *print()*.

![alt text](image-5.png)

---

#### Segue abaixo o comando a para a criação da imagem:

![alt text](image-6.png)

---

#### Segue abaixo o comando usado pada a execução do container e seu teste:

![alt text](image-7.png)

---


