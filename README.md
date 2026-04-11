# API Igreja

## Descrição
API REST para gerenciamento de usuários e posts com autenticação JWT.

## Tecnologias
- FastAPI
- SQLite
- JWT

## Funcionalidades
- Cadastro e login de usuários
- CRUD de posts
- Autenticação com token
- Paginação

## Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload

## Arquitetura

- routers → endpoints (entrada HTTP)
- services → regras de negócio
- repository → acesso ao banco
- core → segurança (JWT, hash, deps)

## Fluxo

Request → Router → Service → Repository → DB

## Autenticação

- login gera JWT
- token enviado no header
- Depends extrai user_id
- rotas usam user autenticado

## Regras importantes

- posts não fazem login
- users não conhecem posts
- auth não acessa banco direto

## Endpoints

### Auth
POST /auth/register
POST /auth/login

### Posts
GET /posts
GET /posts/{id}
POST /posts
PATCH /posts/{id}
DELETE /posts/{id}
