## ETAPA 1:

- Segue abaixo a explicação dos codigos e a evidência do código usado para definir como a imagem será construída:


- Primeiro, a linha *FROM python:3.12.7-slim* define a imagem base do Docker. Em seguida, *WORKDIR /app* estabelece que o diretório de trabalho dentro do container será /app, garantindo que todos os comandos seguintes sejam executados nesse diretório. O comando *COPY carguru.py .* copia o arquivo carguru.py do sistema local para o diretório */app* dentro do container. Por fim, *CMD ["python", "carguru.py"]* define o comando a ser executado quando o container for iniciado, que é rodar o arquivo carguru.py utilizando o Python.

![ETAPA_1_DESAFIO_CODIGO](https://github.com/user-attachments/assets/f6507907-c12b-498d-a5cd-5bd972a6b91c)


---

#### Abaixo, segue-se a evidência da criação da imagem:

![ETAPA_1_DESAFIO_EXECUCAO](https://github.com/user-attachments/assets/5b2beb4c-ac00-47e6-bdf2-96ff22872e2c)


---

#### Após isso, foi feita a execução do container - abaixo segue-se seu resultado:

![ETAPA_1_DESAFIO_EXECUCAO_2](https://github.com/user-attachments/assets/3d7613b5-a3ea-40f2-85e9-6f58cdb5d5bd)



## ETAPA 2:

#### Na etapa dois foi necessário responder as seguintes perguntas: 

![image](https://github.com/user-attachments/assets/c04a957b-2f52-4a0f-a4c4-a45b95255772)


- Respondendo a primeira pergunta: Sim, pode-se reutiliza-lo e pode ser reiniciado sem a necessidade de cria-lo novamente. Reinicia-se através do comando: *docker start*

## ETAPA 3:

- #### Na imagem abaixo é definida a forma como a imagem do script python será construída:

![ETAPA_3_DESAFIO_CODIGO](https://github.com/user-attachments/assets/3f690a07-c27b-46da-9418-0ca27f3e2896)


- obs: os comandos usados para isso foram os mesmos da etapa 1, a alteração feita foi apenas a mudança do nome "carguru" para "script", por ser outra imagem.

#

#### Abaixo, encontra-se a explicação dos comandos e da evidência do algoritmo que recebe uma string, gerando o Hash por meio do algoritmo SH4, e que por fim exibe a Hash em tela usando o método *hexdigest*.

- Primeiramente, o módulo *hashlib* é importado para permitir o uso de funções de hash, como SHA-1. Em seguida, um loop infinito *while True* é utilizado para que o programa continue pedindo entradas indefinidamente. O programa solicita ao usuário que digite uma string com *input()* e essa string é transformada em um *hash SHA-1* usando *hashlib.sha1()*, que converte a string em bytes com *.encode()* e, finalmente, gera a representação em hexadecimal com *hexdigest()*. Por fim, o valor do hash gerado é exibido com *print()*.

![ETAPA_3_DESAFIO_CODIGO_PYTHON](https://github.com/user-attachments/assets/4c8d01b1-cb82-4fa7-8d38-e0e1477d29f7)

---

#### Segue abaixo o comando a para a criação da imagem:

![ETAPA_3_DESAFIO_EXECUCAO](https://github.com/user-attachments/assets/c150c86a-5f18-4b43-824a-10ca6c405fca)

---

#### Segue abaixo o comando usado pada a execução do container e seu teste:

![ETAPA_3_DESAFIO_TESTES](https://github.com/user-attachments/assets/66ad8825-3295-4be2-bd4e-b8d0a117d500)

---


