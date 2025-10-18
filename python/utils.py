import re
from faker import Faker
from csv import DictWriter, DictReader

faker = Faker("pt_BR")


def formatar_dinheiro(valor: float) -> str:
    """ Formata um valor numérico como uma string de dinheiro em reais.

    Parameters:
        valor (float): O valor numérico a ser formatado.

    Returns:
        str: O valor formatado como uma string de dinheiro em reais.
    """

    valor = round(valor, 2)
    return f"R$ {valor:,.2f}".replace(",", "|").replace(".", ",").replace("|", ".")


def calcular_taxa_conclusao(aulas_concluidas: int, total_aulas: int) -> float:
    """ Calcula a taxa de conclusão de um curso.

    Parameters:
        aulas_concluidas (int): Número de aulas concluídas.
        total_aulas (int): Número total de aulas no curso.

    Returns:
        float: A taxa de conclusão como uma porcentagem.
    """

    if total_aulas == 0:
        return 0.0
    return (aulas_concluidas / total_aulas) * 100


def validar_email(email: str) -> bool:
    """ Valida o formato de um endereço de e-mail.

    Parameters:
        email (str): O endereço de e-mail a ser validado.

    Returns:
        bool: True se o e-mail for válido, False caso contrário.
    """

    if len(email) == 0:
        return False

    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email) is not None


def gerar_senha_hash() -> str:
    """ Simula a geração de um hash para uma senha.

    Parameters:
        senha (str): A senha a ser "hashada".

    Returns:
        str: Uma string simulando o hash da senha.
    """

    return faker.md5()


def formatar_data(data) -> str:
    """ Formata uma data no formato 30/01/2020 18:30:56.

    Parameters:
        data (datetime): A data a ser formatada.

    Returns:
        str: A data formatada.
    """

    return data.strftime("%d/%m/%Y %H:%M:%S")


def criar_arquivo_csv(nome_arquivo: str, dados: list, fieldnames: list):
    with open("./data/"+nome_arquivo+".csv", mode="a", newline="", encoding="utf-8") as arquivo:
        writer = DictWriter(arquivo, fieldnames=fieldnames, delimiter=";")

        if arquivo.tell() == 0:
            writer.writeheader()

        for item in dados:
            writer.writerow(item)


def ler_arquivo_csv(nome_arquivo: str) -> list:
    try:
        with open("./data/"+nome_arquivo+".csv", mode="r", encoding="utf-8") as arquivo:
            reader = DictReader(arquivo, delimiter=";")
            return list(reader)
    except FileNotFoundError:
        return []
    except Exception as err:
        print(f"Erro ao ler o arquivo {nome_arquivo}: {err}")
        return []


def buscar_id_aleatorio(nome_tabela: str) -> int | None:
    registros = ler_arquivo_csv(nome_tabela)

    if not registros:
        return None

    indice_aleatorio = faker.random_int(min=0, max=len(registros)-1)
    return registros[indice_aleatorio]["id"]


def gerar_email(primeiro_nome: str, ultimo_nome: str) -> str:
    nome_formatado = primeiro_nome.split(' ')[0]
    sobrenome_formatado = ultimo_nome.split(' ')[-1]

    nome_email = f"{nome_formatado}.{sobrenome_formatado}".lower()
    email = f"{nome_email}@{faker.free_email_domain()}"

    return email
