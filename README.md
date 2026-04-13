API Igreja

Backend desenvolvido com FastAPI para gerenciamento de usuários e posts, com autenticação via JWT e controle de acesso.


● Funcionalidades

- Cadastro e autenticação de usuários
- Geração de token JWT
- CRUD de posts
- Proteção de rotas (autorização por usuário)
- Paginação de resultados
- Padronização de respostas da API



● Autenticação

A API utiliza JWT (JSON Web Token).

Fluxo:

1. Usuário realiza login
2. Recebe um token
3. Envia token nas rotas protegidas via:

Authorization: Bearer <token>



● Estrutura do Projeto

routers/       → rotas da API
services/      → regras de negócio
repository/    → acesso ao banco
models/        → schemas (Pydantic)
core/          → segurança (JWT, hash)



● Tecnologias

- FastAPI
- SQLite
- Pydantic
- Passlib
- Uvicorn



● Deploy

API publicada via Render.



● Melhorias futuras (Backend)

- [ ] Uso de variáveis de ambiente (.env)
- [ ] Expiração e refresh token
- [ ] Tratamento global de exceções
- [ ] Logs estruturados
- [ ] Testes automatizados
- [ ] Migração de SQLite para PostgreSQL
- [ ] Dockerização da aplicação


● Funcionalidades futuras

- [ ] Sistema de newsletter (inscrição de usuários)
- [ ] Envio de notificações
- [ ] Sistema de eventos (ex: novo post gera aviso)


● Aprendizados

Este projeto foi desenvolvido com foco em aprendizado de backend, incluindo:

- Arquitetura em camadas
- Autenticação e autorização
- Consumo de API via Swagger
- Deploy em ambiente cloud


● Autora

Projeto desenvolvido por Thais
