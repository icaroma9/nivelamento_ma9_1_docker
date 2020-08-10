# Nivelamento 1

Aplicação de containers do Docker ao projeto de nivelamento para o cargo de Desenvolvedor Python (DRF).

## Containers

### NGINX 

- Conecta ao Gunicorn e serve como proxy reverso para as solicitações HTTP
- Recebe requisições na porta 80
- Pertence a rede nginx_network

### WEB
- Executa o Gunicorn + Django em modo de produção
- Os arquivos estáticos são servidos pelo próprio Django graças à biblioteca [Whitenoise](https://pypi.org/project/whitenoise/)
- Monta um volume conectado ao diretório raiz do projeto
- Pertence as duas redes nginx_network e db_network

##### Dockerfile
- Instala a versão 3.7 do Python e dependências do projeto

### DB
- Usa a imagem do PostgreSQL
- Banco é configurado através das variáveis de ambiente presentes no arquivo .env na raiz do projeto
- usa o volume pgdata para persistir alterações no banco de dados
- Pertence a rede db_network

## Sobre o docker-compose.yml
- A execução dos comandos envolvendo o Django espera a inicialização completa do Postgres.
- Após a confirmação de que o banco foi inicializado, os arquivos estáticos são coletados, as migrações são executadas, um superusuário é criado e, por fim, o Gunicorn é executado com o Django          
          
## Como executar
1. Clonar repositório
2. Configurar variáveis de ambiente em um arquivo .env na raiz do projeto:
- SECRET_KEY: chave do Django
- DEBUG: flag para ambiente de desenvolvimento
- SU_USERNAME: usuário do superusuário para ser adicionado automaticamente
- SU_EMAIL: email do superusuário para ser adicionado automaticamente
- SU_PASSWORD: senha do superusuário para ser adicionado automaticamente
- POSTGRES_DB: nome do banco de dados
- POSTGRES_USER: usuário do banco de dados
- POSTGRES_PASSWORD: senha do usuário do banco de dados
- POSTGRES_HOST: host do serviço de banco de dados
- POSTGRES_PORT: porta do serviço de banco de dados
3. Executar `docker-compose up --build`
