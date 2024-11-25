# Usa o Amazon Linux 2023 como base.
FROM amazonlinux:2023

# Atualiza os pacotes do sistema.
RUN yum update -y

# Instala o pip para Python e a ferramenta zip.
RUN yum install -y \
    python3-pip \
    zip

# Limpa arquivos temporários para reduzir o tamanho da imagem.
RUN yum -y clean all
