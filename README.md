# Projeto EduTech: Plataforma de Gerenciamento de Cursos

##  Índice

- [Projeto EduTech: Plataforma de Gerenciamento de Cursos](#projeto-edutech-plataforma-de-gerenciamento-de-cursos)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Modelagem do Banco de Dados](#modelagem-do-banco-de-dados)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Estrutura do Projeto](#estrutura-do-projeto)
  - [Fluxo de Execução](#fluxo-de-execução)
  - [Como Configurar e Executar o Projeto](#como-configurar-e-executar-o-projeto)
    - [1. Pré-requisitos](#1-pré-requisitos)
    - [2. Configuração do Ambiente](#2-configuração-do-ambiente)
    - [3. Execução Passo a Passo](#3-execução-passo-a-passo)

---

## Visão Geral

O projeto EduTech simula o backend de uma plataforma de cursos online. O objetivo principal é demonstrar a criação de um banco de dados relacional robusto com PostgreSQL, a automação de tarefas com scripts Python e a orquestração do ambiente de desenvolvimento utilizando Docker.

O sistema gerencia entidades como alunos, instrutores, cursos, matrículas e progresso, formando a base para uma aplicação de e-learning funcional.

## Modelagem do Banco de Dados

A estrutura do banco de dados foi projetada para garantir a integridade e a consistência dos dados. As principais entidades incluem:

-   **Alunos:** Gerencia as informações dos usuários que consomem o conteúdo.
-   **Instrutores:** Armazena dados dos responsáveis pela criação dos cursos.
-   **Cursos:** Contém os detalhes de cada curso oferecido.
-   **Módulos e Aulas:** Estruturam o conteúdo de cada curso.
-   **Matrículas e Progresso:** Rastreiam a inscrição e o avanço dos alunos nos cursos.

O Diagrama Entidade-Relacionamento (ER) detalhado pode ser encontrado em `docs/diagrama_er.png`.

## Tecnologias Utilizadas

-   **Banco de Dados:** PostgreSQL
-   **Linguagem de Script:** Python 3.x
-   **Containerização:** Docker & Docker Compose
-   **Bibliotecas Python:**
    -   `Faker`: Geração de dados fictícios (mock).

## Estrutura do Projeto

```
.
├── data/              # Armazena os arquivos .csv gerados para carga de dados.
├── docs/              # Contém a documentação (ex: Diagrama ER).
├── python/            # Scripts Python para automação.
│   ├── gerador_dados.py # Gera dados fictícios e salva em .csv.
│   ├── main.py          # Orquestra a carga dos dados .csv para o banco.
│   └── utils.py         # Funções utilitárias (ex: conexão com o BD).
├── sql/               # Scripts SQL.
│   └── schema.sql       # Define a estrutura completa do banco de dados (DDL).
├── .env               # Arquivo de configuração de variáveis de ambiente (local).
├── docker-compose.yml # Define o serviço do banco de dados PostgreSQL.
└── requirements.txt   # Lista de dependências Python.
```

## Fluxo de Execução

1.  **Ambiente:** O `docker-compose` inicializa um container com o PostgreSQL.
2.  **Criação do Schema:** O script `sql/schema.sql` é executado para criar todas as tabelas, tipos e relacionamentos no banco de dados.
3.  **Geração de Dados:** O script `python/gerador_dados.py` cria dados fictícios e os armazena em arquivos `.csv` no diretório `data/`.
4.  **Carga de Dados:** O script `python/main.py` lê os arquivos `.csv` e insere os dados em massa nas tabelas correspondentes do PostgreSQL.

## Como Configurar e Executar o Projeto

### 1. Pré-requisitos

-   [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/) instalados.
-   [Python 3.x](https://www.python.org/downloads/) instalado.
-   [Git](https://git-scm.com/) instalado.

### 2. Configuração do Ambiente

**a. Clone o Repositório**
```sh
git clone https://github.com/JessicaSilvaSoares/EduTech
cd EduTech
```

**b. Crie o Arquivo de Ambiente**

Crie um arquivo `.env` na raiz do projeto e preencha com as credenciais do banco de dados. Estes valores devem ser os mesmos definidos em `docker-compose.yml`.

```env
# .env
POSTGRES_USER=
PGPASSWORD=
POSTGRES_PORT=
```

### 3. Execução Passo a Passo

**a. Crie o ambiente para execução dos scripts**

Este comando irá criar e iniciar o container do PostgreSQL em segundo plano e criar o ambiente virtual.

```sh
make run
```

**b. Gere os Dados Fictícios**

Este comando irá popular a pasta `data/` com arquivos `.csv`.

```sh
make gerar-dados
```

**c. Valide os Dados**

Este comando irá validar os arquivos `.csv` da pasta `data/`.

```sh
make validar-dados
```

**d. Carregue os Dados no Banco**

Execute o script principal para inserir os dados dos arquivos `.csv` nas tabelas do PostgreSQL.

```sh
make importar-dados
```

Ao final desses passos, o banco de dados estará totalmente configurado, estruturado e populado, pronto para ser consultado.