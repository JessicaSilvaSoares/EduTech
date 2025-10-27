# Documentação dos Comandos `make`

Este documento descreve os comandos disponíveis no `Makefile` do projeto para automatizar as tarefas de configuração, execução e limpeza do ambiente.

---

## Comandos Principais

### `make run`

Prepara e inicia o ambiente de desenvolvimento completo. Este é um comando composto que executa as seguintes regras em sequência: `docker-up`, `activate` e `criar-schema`.

**Ações Executadas:**
1.  Inicia o container do PostgreSQL em segundo plano.
2.  Cria o ambiente virtual Python e instala as dependências.
3.  Executa o script `sql/schema.sql` para criar a estrutura do banco de dados.

**Uso:**
```sh
make run
```

---

## Comandos de Ambiente

### `make docker-up`

Inicia o serviço do banco de dados PostgreSQL definido no `docker-compose.yml`.

**Uso:**
```sh
make docker-up
```

### `make activate`

Cria o ambiente virtual Python no diretório `.venv` (se não existir) e instala as dependências listadas em `requirements.txt`.

**Uso:**
```sh
make activate
```

### `make deactivate`

Remove o diretório do ambiente virtual (`.venv`).

**Uso:**
```sh
make deactivate
```

---

## Comandos de Dados

### `make gerar-dados`

Executa o script `python/gerador_dados.py` para criar dados fictícios e salvá-los como arquivos `.csv` no diretório `data/`.

**Uso:**
```sh
make gerar-dados
```

### `make validar-dados`

Executa o script `python/validador_csv.py` para verificar a integridade e o formato dos arquivos `.csv` gerados. Um `relatorio_erros.md` será criado se forem encontrados problemas.

**Uso:**
```sh
make validar-dados
```

### `make importar-dados`

Executa o script `sql/import.sql` dentro do container do banco de dados para carregar os dados dos arquivos `.csv` nas tabelas do PostgreSQL.

**Uso:**
```sh
make importar-dados
```

---

## Comandos de Banco de Dados

### `make criar-schema`

Executa o script `sql/schema.sql` para criar todas as tabelas, tipos e relacionamentos no banco de dados.

**Uso:**
```sh
make criar-schema
```

### `make remover-schema`

Executa o script `sql/remove_schema.sql` para remover todas as tabelas e tipos criados no banco de dados.

**Uso:**
```sh
make remover-schema
```

### `make popular-banco`

Executa o script `sql/dados.sql` para popular o banco de dados com um conjunto de dados pré-definido.

**Uso:**
```sh
make popular-banco
```

---

## Comandos de Limpeza e Reconstrução

### `make clean`

Remove os arquivos gerados durante a execução, como os `.csv` da pasta `data/` e o `relatorio_erros.md`.

**Uso:**
```sh
make clean
```

### `make fclean`

Realiza uma limpeza completa do ambiente.

**Ações Executadas:**
1.  Remove o schema do banco de dados (`remover-schema`).
2.  Remove o ambiente virtual (`deactivate`).
3.  Remove os arquivos gerados (`clean`).
4.  Para e remove os containers, volumes e redes do Docker (`docker compose down`).

**Uso:**
```sh
make fclean
```

### `make re`

Reconstrói o ambiente do zero. É um atalho para executar `fclean` e depois `run`.

**Uso:**
```sh
make re
```