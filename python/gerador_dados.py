from faker import Faker
from datetime import date, datetime
from utils import criar_arquivo_csv, ler_arquivo_csv, buscar_id_aleatorio, gerar_email
from json import load

fake = Faker("pt_BR")


def gerar_alunos(quantidade: int):
    alunos = []

    for index in range(quantidade):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        email = gerar_email(nome, sobrenome)

        aluno = {
            "id": index + 1,
            "nome": f"{nome} {sobrenome}",
            "email": email,
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=50).strftime("%Y-%m-%d"),
            "ativo": fake.boolean(chance_of_getting_true=95),
            "data_cadastro": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S")
        }
        alunos.append(aluno)

    return alunos


def gerar_instrutores(quantidade: int):
    instrutores = []

    for index in range(quantidade):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        email = gerar_email(nome, sobrenome)

        instrutor = {
            "id": index + 1,
            "nome": f"{nome} {sobrenome}",
            "email": email,
            "biografia": fake.text(max_nb_chars=200),
            "ativo": fake.boolean(chance_of_getting_true=95),
            "data_cadastro": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S")
        }
        instrutores.append(instrutor)

    return instrutores


def gerar_cursos(quantidade: int):
    cursos = []

    for index in range(quantidade):
        id_instrutor = buscar_id_aleatorio("instrutores")
        id_categoria = buscar_id_aleatorio("categorias")
        id_nivel = buscar_id_aleatorio("cursos_nivel")

        curso = {
            "id": index + 1,
            "titulo": fake.sentence(nb_words=4),
            "descricao": fake.text(max_nb_chars=100),
            "preco": fake.pydecimal(left_digits=3, right_digits=2, positive=True, min_value=50, max_value=500),
            "carga_horaria": fake.random_int(min=20, max=200) * 60, # a duração do curso é registrada em minutos
            "id_instrutor": id_instrutor,
            "id_categoria": id_categoria,
            "id_nivel": id_nivel,
            "data_cadastro": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S"),
        }
        cursos.append(curso)

    return cursos


def gerar_aulas(curso_id: int, quantidade: int):
    modulos = []
    aulas = []

    qtd_modulos = fake.random_int(min=2, max=quantidade//3 if quantidade >=6 else quantidade)
    aula_index = 0

    old_modulos = ler_arquivo_csv("modulos")
    if len(old_modulos) > 0:
        modulo_index = int(old_modulos[-1]["id"])
    else:
        modulo_index = 0

    old_aulas = ler_arquivo_csv("aulas")
    if len(old_aulas) > 0:
        aula_index = int(old_aulas[-1]["id"])
    else:
        aula_index = 0

    for index in range(qtd_modulos):
        
        modulo = {
            "id": modulo_index + 1,
            "titulo": fake.sentence(nb_words=4),
            "descricao": fake.text(max_nb_chars=200),
            "id_curso": curso_id,
            "ordem": index + 1
        }
        modulos.append(modulo)
        modulo_index += 1

        for ordem_modulo_aula in range(quantidade // qtd_modulos):
            id_tipo = buscar_id_aleatorio("aulas_tipo")

        aula = {
            "id": aula_index + 1,
            "titulo": fake.sentence(nb_words=6),
            "descricao": fake.text(max_nb_chars=200),
            "duracao": fake.random_int(min=30, max=120), # duracao em minutos
            "ordem": ordem_modulo_aula + 1,
            "id_modulo": modulo["id"],
            "id_tipo": id_tipo,
            "data_cadastro": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S"),
        }
        aula_index += 1

        aulas.append(aula)
        qtd_modulos -= 1

    return modulos, aulas


def gerar_matriculas(quantidade: int):
    matriculas = []

    matriculas_status = ler_arquivo_csv("matriculas_status")

    for index in range(quantidade):
        id_aluno = buscar_id_aleatorio("alunos")
        id_curso = buscar_id_aleatorio("cursos")
        id_status = buscar_id_aleatorio("matriculas_status")

        matricula = {
            "id": index + 1,
            "id_aluno": id_aluno,
            "id_curso": id_curso,
            "id_status": id_status,
            "data_matricula": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S"),
        }

        if fake.boolean(chance_of_getting_true=50):
            matricula["data_conclusao"] = fake.date_time_between_dates(
                datetime_start=datetime.strptime(matricula["data_matricula"], "%Y-%m-%dT%H:%M:%S"),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S")

            matriculas_status_concluido = [status for status in matriculas_status if status["status"].lower() == "concluída"]
            if matriculas_status_concluido:
                matricula["id_status"] = matriculas_status_concluido[0]["id"]
        else:
            matricula["data_conclusao"] = None

        matriculas.append(matricula)
    return matriculas


def gerar_avaliacoes(quantidade: int):
    avaliacoes = []

    for index in range(quantidade):
        matriculas = ler_arquivo_csv("matriculas")
        matricula = matriculas[fake.random_int(min=0, max=len(matriculas)-1)]

        id_curso = matricula["id_curso"]
        id_matricula = matricula["id"]

        avaliacao = {
            "id": index + 1,
            "id_curso": id_curso,
            "id_matricula": id_matricula,
            "nota": fake.random_int(min=1, max=5),
            "comentario": fake.text(max_nb_chars=500),
            "data_avaliacao": fake.date_time_between_dates(
                datetime_start=date(2023, 1, 1),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S"),
        }
        avaliacoes.append(avaliacao)

    return avaliacoes 


def gerar_progresso_aulas(quantidade: int):
    progresso_aulas = []

    for index in range(quantidade):
        matriculas = ler_arquivo_csv("matriculas")
        matricula = matriculas[fake.random_int(min=0, max=len(matriculas)-1)]

        id_curso = matricula["id_curso"]
        modulos = ler_arquivo_csv("modulos")
        modulos = [modulo for modulo in modulos if modulo["id_curso"] == id_curso]

        aulas = ler_arquivo_csv("aulas")
        aulas_curso = []
        for modulo in modulos:
            aulas_modulo = [aula for aula in aulas if aula["id_modulo"] == modulo["id"]]
            aulas_curso.extend(aulas_modulo)        

        aula_escolhida = aulas_curso[fake.random_int(min=0, max=len(aulas_curso)-1)]

        progresso = {
            "id": index + 1,
            "id_matricula": matricula["id"],
            "id_aula": aula_escolhida["id"],
            "tempo_assistido": fake.random_int(min=0, max=int(aula_escolhida["duracao"])),
            "concluido": fake.boolean(chance_of_getting_true=45),
            "data_conclusao": None
        }

        if progresso["concluido"]:
            progresso["tempo_assistido"] = int(aula_escolhida["duracao"])
            progresso["data_conclusao"] = fake.date_time_between_dates(
                datetime_start=datetime.strptime(matricula["data_matricula"], "%Y-%m-%dT%H:%M:%S"),
                datetime_end=date(2025, 10, 15),
                tzinfo=None
            ).strftime("%Y-%m-%dT%H:%M:%S")

        progresso_aulas.append(progresso)
    return progresso_aulas


def gerar_arquivos_estaticos():
    dados = load(open("./data/dados.json", mode="r", encoding="utf-8"))

    criar_arquivo_csv("aulas_tipo", dados["aulas_tipo"], ["id","tipo"])
    criar_arquivo_csv("cursos_nivel", dados["cursos_nivel"], ["id","nivel"])
    criar_arquivo_csv("matriculas_status", dados["matriculas_status"], ["id","status"])
    criar_arquivo_csv("categorias", dados["categorias"], ["id","nome","descricao"])
    criar_arquivo_csv("especialidades", dados["especialidades"], ["id","especialidade"])


def exportar_para_csv():
    gerar_arquivos_estaticos()

    criar_arquivo_csv("alunos", gerar_alunos(30), ["id","nome","email","data_nascimento","ativo","data_cadastro"])
    criar_arquivo_csv("instrutores", gerar_instrutores(10), ["id","nome","email","biografia","ativo","data_cadastro"])

    cursos = gerar_cursos(20)
    criar_arquivo_csv("cursos", cursos, ["id","titulo","descricao","preco","carga_horaria","id_instrutor","id_categoria","id_nivel","data_cadastro"])

    for curso in cursos:
        modulos, aulas = gerar_aulas(curso["id"], fake.random_int(min=2, max=10))
        criar_arquivo_csv("modulos", modulos, ["id","titulo","descricao","id_curso","ordem"])
        criar_arquivo_csv("aulas", aulas, ["id","titulo","descricao","duracao","ordem","id_modulo","id_tipo","data_cadastro"])


    criar_arquivo_csv("matriculas", gerar_matriculas(80), ["id","id_aluno","id_curso","id_status","data_matricula","data_conclusao"])
    criar_arquivo_csv("avaliacoes", gerar_avaliacoes(100), ["id","id_curso","id_matricula","nota","comentario","data_avaliacao"])
    criar_arquivo_csv("progresso_aulas", gerar_progresso_aulas(80), ["id","id_matricula","id_aula", "tempo_assistido","concluido","data_conclusao"])


if __name__ == "__main__":
    exportar_para_csv()