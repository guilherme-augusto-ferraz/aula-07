# Aula 07 — Aplicação Flask

Este repositório contém uma aplicação web construída com Flask usada na aula 07. A aplicação usa SQLite para persistência, autenticação JWT e bcrypt para hash de senhas.

Resumo rápido (extraído do código):
- Arquivo principal: `app/app.py`
- Blueprints registrados:
  - `/api/usuarios` — blueprint `usuarios_bp` (rotas de usuário)
  - `/api/tarefas` — blueprint `tarefas_bp` (rotas de tarefas)
- Banco de dados: `sqlite:///database.db` (criado automaticamente)
- Bibliotecas principais: Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-JWT-Extended

Trechos relevantes do código (para referência)
```python
# app/app.py
app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
app.register_blueprint(tarefas_bp, url_prefix='/api/tarefas')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'chave-super-secreta'  # troque em produção
```

O que este projeto faz
- Fornece endpoints agrupados em dois blueprints:
  - `/api/usuarios` — gerenciamento/autenticação de usuários (registro, login, CRUD de usuário, etc.)
  - `/api/tarefas` — CRUD de tarefas (criar, listar, atualizar, apagar)
- Usa JWT para proteger rotas (acesso via header Authorization: Bearer <token>)
- Armazena dados em um SQLite local (`database.db`)

Onde olhar o código das rotas
- `app/routes/usuarios.py` — todas as rotas relacionadas a usuários
- `app/routes/tarefas.py` — todas as rotas relacionadas a tarefas

Como executar localmente

1. Clone o repositório e entre na pasta `app`:
   git clone https://github.com/guilherme-augusto-ferraz/aula-07.git
   cd aula-07/app

2. Crie e ative um ambiente virtual (recomendado):
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

3. Instale dependências:
   pip install -r requirements.txt

4. Execute a aplicação:
   python app.py
   Por padrão a aplicação roda em http://127.0.0.1:5000/ com debug=True.

Observações sobre o banco e inicialização
- O banco SQLite (`database.db`) é criado automaticamente ao iniciar a aplicação (veja `db.create_all()` em `app/app.py`).
- A JWT secret key está definida em `app/app.py` como `chave-super-secreta`. Altere em produção.

Rotas e exemplos de chamadas (modelos)
- As rotas exatas (paths de cada recurso, nomes de parâmetros e payloads) estão definidas nos arquivos de rota mencionados acima. Aqui seguem exemplos genéricos de como fazer chamadas com base nos prefixes reais registrados:

1) Exemplos para `/api/usuarios` (substitua os caminhos concretos conforme definidos em `routes/usuarios.py`)

- Registrar/criar usuário (exemplo genérico):
  curl -X POST http://127.0.0.1:5000/api/usuarios -H "Content-Type: application/json" -d '{"nome":"Fulano","email":"fulano@ex.com","senha":"senha"}'

- Login (exemplo genérico — retorna token JWT):
  curl -X POST http://127.0.0.1:5000/api/usuarios/login -H "Content-Type: application/json" -d '{"email":"fulano@ex.com","senha":"senha"}'

- Listar usuários (se houver rota):
  curl http://127.0.0.1:5000/api/usuarios

2) Exemplos para `/api/tarefas` (substitua os caminhos concretos conforme definidos em `routes/tarefas.py`)

- Listar tarefas:
  curl http://127.0.0.1:5000/api/tarefas

- Criar tarefa (exemplo com autenticação JWT):
  curl -X POST http://127.0.0.1:5000/api/tarefas -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>" -d '{"titulo":"Estudar","descricao":"Ler Flask"}'

- Atualizar / deletar tarefa:
  curl -X PUT http://127.0.0.1:5000/api/tarefas/<id> -H "Authorization: Bearer <TOKEN>" -d '{"titulo":"..."}'
  curl -X DELETE http://127.0.0.1:5000/api/tarefas/<id> -H "Authorization: Bearer <TOKEN>"

Autenticação
- A aplicação usa Flask-JWT-Extended. Se uma rota requer autenticação, envie o header:
  Authorization: Bearer <access_token>
- Normalmente o token é obtido no endpoint de login (ver `routes/usuarios.py`).

Como testar rapidamente
- Importar `Insomnia_2025-10-31.yaml` (presente na pasta `app/`) em Insomnia/Postman — o arquivo já contém coleções/export das rotas para facilitar testes.
- Usar `curl` com os modelos acima, adaptando os paths/JSON conforme as implementações concretas nos arquivos `routes/*`.

Execução de testes automatizados
- Não há testes automatizados no diretório `app/` por padrão. Caso adicione testes, rode com:
  python -m unittest
  ou com o runner que for incluído (pytest).

Arquivos importantes
- `app/app.py` — criação da app, registro de blueprints e configuração
- `app/database.py` — inicialização do objeto `db` (SQLAlchemy)
- `app/models/` — modelos SQLAlchemy (ex.: `usuario.py`, `tarefa.py`)
- `app/routes/` — definição das rotas reais (`usuarios.py`, `tarefas.py`)
- `app/requirements.txt` — dependências
- `app/Insomnia_2025-10-31.yaml` — coleção para importar em Insomnia/Postman

Boas práticas e próximos passos
- Trocar `JWT_SECRET_KEY` por variável de ambiente em produção.
- Adicionar validação de entradas (schemas) e tratamento de erros detalhado.
- Adicionar testes automatizados para endpoints e modelos.

Se quiser, eu posso:
- Abrir e extrair a lista exata de endpoints (métodos e paths) lendo `app/routes/usuarios.py` e `app/routes/tarefas.py` e inserir exemplos concretos de payloads e respostas no README.
- Gerar exemplos prontos de requests (curl/Insomnia) com base nas rotas reais encontradas nos arquivos.
