DOCKER_EXEC=docker compose exec -T

DOCKER_CONTAINER=db

PSQL_VARIABLES=--username=$$POSTGRES_USER --dbname=$$POSTGRES_DB --port=$$POSTGRES_PORT

ENV_FILE=.env

VENV=.venv

PYTHON=$(VENV)/bin/python3

PIP=$(VENV)/bin/pip


# REGRAS PARA CRIAR O AMBIENTE

run: docker-up activate criar-schema

# SOBE O BANCO DE DADOS
docker-up:
	@ docker compose up -d

# CRIA O AMBIENTE VIRTUAL E INSTALAR AS DEPENDÊNCIAS
activate:
	@ find $(VENV) -false 2>/dev/null || echo "Criando ambiente virtual..." && python3 -m venv $(VENV)
	@ find $(VENV)/bin/faker -false 2>/dev/null || (echo "Baixando dependencias...\n" && $(PIP) install -r requirements.txt)

# REMOVE O AMBIENTE VIRTUAL
deactivate:
	@ rm -rf $(VENV)
	@ echo "Ambiente virtual removido"


# REGRAS PARA EXECUTAR OS SCRIPTS EM PYTHON PARA GERAR E VALIDAR DADOS

# GERA DADOS FICTICIOS EM ARQUIVOS CSV
gerar-dados: activate
	@ ($(PYTHON) python/gerador_dados.py && echo "Dados gerados com sucesso!") || (echo "\nErro ao gerar dados.")

# VALIDA OS DADOS GERADOS
validar-dados: activate
	@ rm -f relatorio_erros.md
	@ ($(PYTHON) python/validador_csv.py && echo "Dados validados com sucesso!") || (echo "\nErro ao validar dados.")

# IMPORTA OS DADOS VALIDADOS PARA O BANCO DE DADOS
importar-dados: activate
	@ cat ./sql/import.sql | $(DOCKER_EXEC) --env $(ENV_FILE) $(DOCKER_CONTAINER)  sh -c 'psql $(PSQL_VARIABLES)'


# REGRAS PARA INTERAGIR COM O BANCO DE DADOS

# CRIA O SCHEMA NO BANCO DE DADOS
criar-schema:
	@ cat ./sql/schema.sql | $(DOCKER_EXEC) --env $(ENV_FILE) $(DOCKER_CONTAINER)  sh -c 'psql $(PSQL_VARIABLES)'

# POPULA O BANCO DE DADOS COM SCRIPT SQL
popular-banco:
	@ cat ./sql/dados.sql | $(DOCKER_EXEC) --env $(ENV_FILE) $(DOCKER_CONTAINER)  sh -c 'psql $(PSQL_VARIABLES)'

# REMOVE O SCHEMA DO BANCO DE DADOS
remover-schema:
	@ cat ./sql/remove_schema.sql | $(DOCKER_EXEC) --env $(ENV_FILE) $(DOCKER_CONTAINER)  sh -c 'psql $(PSQL_VARIABLES)'


# LIMPA OS ARQUIVOS GERADOS
clean:
	@ rm -f data/*.csv relatorio_erros.md

# LIMPA TODO O AMBIENTE CRIADO
fclean: remove_schema deactivate clean
	@ docker compose down --volumes --remove-orphans
	@ rm -f data/*.csv relatorio_erros.md

re: fclean run

.PHONY: run, docker-up, activate, deactivate, gerar-dados, validar-dados, importar-dados, criar-schema, popular-banco, remover-schema, clean, fclean, re