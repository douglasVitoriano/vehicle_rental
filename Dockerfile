# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /src

# Copiar o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Expor a porta em que a aplicação vai rodar
EXPOSE 8000

# Definir o comando padrão para executar a aplicação
CMD ["python", "src/main.py"]
