# Igreja API
Aplicação backend desenvolvida em Python e FastAPI para gerenciamento de avisos
paroquiais.
O projeto foi criado como estudo de arquitetura de APIs e boas práticas de
desenvolvimento, utilizando autenticação JWT, organização em camadas (Routers, Services
e Repository) e banco de dados SQLite.
Além do backend, o projeto prevê uma interface web em desenvolvimento, com o objetivo de
evoluir para uma Progressive Web App (PWA), permitindo que comunidades paroquiais
publiquem e consultem avisos de forma simples.

## Objetivos do projeto
- Estudar desenvolvimento de APIs com FastAPI.
- Aplicar arquitetura em camadas.
- Implementar autenticação utilizando JWT.
- Praticar modelagem de banco de dados com SQLite.
- Desenvolver uma base para evolução de uma aplicação PWA.

## Tecnologias

- Python
- FastAPI
- SQLite
- JWT Authentication
- Uvicorn
- HTML/CSS/JavaScript
- Render
- GitHub

---

# Funcionalidades

## Usuários
- Cadastro
- Login com JWT
- Listagem
- Desativação lógica

## Posts
- Criar posts autenticados
- Atualizar posts
- Deletar posts
- Listagem com paginação
- Busca por título

## Newsletter
- Cadastro de emails
- Listagem de inscritos

---

# Estrutura do projeto
O projeto foi organizado utilizando separação de responsabilidades:

```bash
app/
├── core/
├── models/
├── repository/
├── routers/
├── services/
├── main.py
└── igreja.db
```
Essa organização facilita a manutenção, os testes e a evolução da aplicação conforme novas funcionalidades são adicionadas.

---

# Instalação

## Clonar projeto

```bash
git clone git@github.com:thaisiguibi/Igreja.git
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

### Linux / Termux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Variáveis de ambiente

Criar arquivo `.env`

```env
SECRET_KEY=sua_chave
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Rodar aplicação

```bash
uvicorn main:app --reload
```

---

# Documentação Swagger

Acesse:

```txt
http://127.0.0.1:8000/docs
```

---

# Autenticação

A API utiliza JWT Bearer Token.

Fluxo:

1. Registrar usuário
2. Fazer login
3. Copiar access_token
4. Autorizar no Swagger
5. Consumir rotas protegidas

---

# Deploy

Deploy realizado no:

- Render

Versionamento:

- GitHub

---

# Melhorias futuras

- Frontend completo
- Upload de imagens
- Painel administrativo
- Roles de usuário
- Cache
- Docker
- PostgreSQL
- Refresh token
- Rate limiting

---

# Licença

Projeto educacional.

## O que aprendi

Este projeto permitiu praticar:

- Desenvolvimento de APIs REST
- Organização em camadas
- Autenticação JWT
- Modelagem de banco de dados
- Paginação e busca
- Estruturação de projetos Python
