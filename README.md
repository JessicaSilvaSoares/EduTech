# EduTech - Sistema de Gerenciamento de Cursos Online

Este projeto consiste em um sistema de gerenciamento para uma plataforma de cursos online (EduTech), com um forte foco em modelagem de banco de dados com SQL/PostgreSQL e o uso de Python como ferramenta auxiliar para geração de dados e validações.

## Tecnologias Utilizadas

- **Banco de Dados:** PostgreSQL
- **Linguagem de Script:** Python 3.x
- **Containerização:** Docker
- **Dependências Python:** Faker (para geração de dados fictícios)

## Estrutura de Pastas

```
.
├── data/              # Armazena os arquivos .csv gerados pelo Python
├── docs/              # Contém a documentação, como o diagrama ER
├── python/            # Scripts Python para geração de dados, validação e relatórios
|   ├── validador/
│   ├── gerador_dados.py
│   ├── main.py
│   └── utils.py
└── sql/               # Scripts SQL para criação do schema, inserção de dados e consultas
```

## Como Executar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Pré-requisitos

- [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/) instalados.
- [Python 3.x](https://www.python.org/downloads/) instalado.

### 2. Clonar o Repositório

```sh
git clone https://github.com/JessicaSilvaSoares/EduTech
cd EduTech
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo. Substitua os valores de exemplo pelas credenciais definidas no seu arquivo `docker-compose.yml`.

```env
# Exemplo de configuração para o banco de dados PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_DB=edutech
POSTGRES_HOST=localhost
POSTGRES_DRIVER=PostgreSQL Unicode
```

### 4. Iniciar o Banco de Dados com Docker

Execute o comando abaixo para iniciar o container do PostgreSQL em segundo plano.

```sh
docker-compose up -d
```

### 5. Instalar Dependências Python

Crie um ambiente virtual e instale as dependências listadas no `requirements.txt`.

```sh
# Criar e ativar ambiente virtual (Opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 6. Criar o Schema do Banco de Dados

1.  Conecte-se ao banco de dados PostgreSQL usando sua IDE SQL (DBeaver, pgAdmin, etc.). As credenciais de conexão podem ser encontradas no seu arquivo `docker-compose.yml`.
2.  Abra o arquivo `sql/schema.sql`.
3.  Execute o script completo para criar todas as tabelas e seus relacionamentos.

### 7. Gerar Dados Fictícios

Execute o script Python para gerar os dados e exportá-los para arquivos CSV na pasta `data`.

```sh
python python/gerador_dados.py
```
