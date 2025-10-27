from valida_dados import valida_dado
from utils import ler_arquivo_csv

def valida_alunos():
    obrigatorios = ["id", "nome", "email", "data_nascimento", "ativo"]
    unicos = ["id", "email"]
    inteiros = ["id"]
    datas = ["data_nascimento"]
    emails = ["email"]
    erros = []

    alunos = ler_arquivo_csv("alunos")
    for aluno in alunos:
        aluno_erro = {
            "data": aluno,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=alunos, data=aluno, emails=emails, obrigatorios=obrigatorios, unicos=unicos, numeros=inteiros, datas=datas)
        if erros_validacao:
            aluno_erro["erros"].extend(erros_validacao)
            erros.append(aluno_erro)

    return erros


def valida_especialidades():
    obrigatorios = ["id", "especialidade"]
    unicos = ["id", "especialidade"]
    numeros = ["id"]
    erros = []

    especialidades = ler_arquivo_csv("especialidades")
    for especialidade in especialidades:
        especialidade_erro = {
            "data": especialidade,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=especialidades, data=especialidade, obrigatorios=obrigatorios, unicos=unicos, numeros=numeros)
        if erros_validacao:
            especialidade_erro["erros"].extend(erros_validacao)
            erros.append(especialidade_erro)

    return erros


def valida_instrutores():
    obrigatorios = ["id", "nome", "email", "ativo"]
    unicos = ["id", "email"]
    numeros = ["id"]
    emails = ["email"]
    erros = []

    instrutores = ler_arquivo_csv("instrutores")
    for instrutor in instrutores:
        instrutor_erro = {
            "data": instrutor,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=instrutores, data=instrutor, emails=emails, obrigatorios=obrigatorios, unicos=unicos, numeros=numeros)
        if erros_validacao:
            instrutor_erro["erros"].extend(erros_validacao)
            erros.append(instrutor_erro)

    return erros


def valida_especialidades_instrutores():
    obrigatorios = ["id_instrutor", "id_especialidade"]
    unicos_compostos = [["id_instrutor", "id_especialidade"]]
    chaves_estrangeiras = [{
        "key": "id_instrutor", "tabela": "instrutores"
    }, {
        "key": "id_especialidade", "tabela": "especialidades"
    }]
    erros = []
    
    especialidades_instrutores = ler_arquivo_csv("especialidades_instrutores")
    for especialidade_instrutor in especialidades_instrutores:
        especialidade_instrutor_erro = {
            "data": especialidade_instrutor,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=especialidades_instrutores, data=especialidade_instrutor, obrigatorios=obrigatorios, unicos_compostos=unicos_compostos, chaves_estrangeiras=chaves_estrangeiras)
        if erros_validacao:
            especialidade_instrutor_erro["erros"].extend(erros_validacao)
            erros.append(especialidade_instrutor_erro)

    return erros


def valida_categorias():
    obrigatorios = ["id", "nome"]
    unicos = ["id", "nome"]
    numeros = ["id"]
    erros = []

    categorias = ler_arquivo_csv("categorias")
    for categoria in categorias:
        categoria_erro = {
            "data": categoria,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=categorias, data=categoria, obrigatorios=obrigatorios, unicos=unicos, numeros=numeros)
        if erros_validacao:
            categoria_erro["erros"].extend(erros_validacao)
            erros.append(categoria_erro)

    return erros


def valida_cursos_nivel():
    obrigatorios = ["id", "nivel"]
    numeros = ["id"]
    unicos = ["id", "nivel"]
    erros = []

    cursos_nivel = ler_arquivo_csv("cursos_nivel")
    for curso_nivel in cursos_nivel:
        curso_nivel_erro = {
            "data": curso_nivel,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=cursos_nivel, data=curso_nivel, obrigatorios=obrigatorios, numeros=numeros, unicos=unicos)
        if erros_validacao:
            curso_nivel_erro["erros"].extend(erros_validacao)
            erros.append(curso_nivel_erro)

    return erros


def valida_cursos():
    obrigatorios = ["id", "titulo", "descricao", "preco", "carga_horaria", "id_nivel"]
    unicos = ["id", "titulo"]
    numeros = ["id", "id_nivel"]
    chaves_estrangeiras = [
        {"key": "id_nivel", "tabela": "cursos_nivel"},
        {"key": "id_instrutor", "tabela": "instrutores"},
        {"key": "id_categoria", "tabela": "categorias"},
    ]
    erros = []

    cursos = ler_arquivo_csv("cursos")
    for curso in cursos:
        curso_erro = {
            "data": curso,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=cursos, data=curso, obrigatorios=obrigatorios, numeros=numeros, chaves_estrangeiras=chaves_estrangeiras, unicos=unicos)
        if erros_validacao:
            curso_erro["erros"].extend(erros_validacao)
            erros.append(curso_erro)

    return erros


def valida_modulos():
    obrigatorios = ["id", "titulo", "ordem", "id_curso"]
    unicos = ["id", "titulo"]
    unicos_compostos = [["id_curso", "ordem"]]
    numeros = ["id", "id_curso", "ordem"]
    chaves_estrangeiras = [{
        "key": "id_curso", "tabela": "cursos"
    }]
    erros = []

    modulos = ler_arquivo_csv("modulos")
    for modulo in modulos:
        modulo_erro = {
            "data": modulo,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=modulos, data=modulo, obrigatorios=obrigatorios, unicos_compostos=unicos_compostos, numeros=numeros, chaves_estrangeiras=chaves_estrangeiras, unicos=unicos)
        if erros_validacao:
            modulo_erro["erros"].extend(erros_validacao)
            erros.append(modulo_erro)

    return erros


def valida_aulas_tipo():
    obrigatorios = ["id", "tipo"]
    numeros = ["id"]
    unicos = ["id", "tipo"]
    erros = []

    aulas_tipo = ler_arquivo_csv("aulas_tipo")
    for aula_tipo in aulas_tipo:
        aula_tipo_erro = {
            "data": aula_tipo,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=aulas_tipo, data=aula_tipo, obrigatorios=obrigatorios, numeros=numeros, unicos=unicos)
        if erros_validacao:
            aula_tipo_erro["erros"].extend(erros_validacao)
            erros.append(aula_tipo_erro)

    return erros


def valida_aulas():
    obrigatorios = ["id", "titulo", "duracao", "id_tipo", "id_modulo"]
    numeros = ["id", "duracao", "id_tipo", "id_modulo"]
    unicos = ["id", "titulo"]
    unicos_compostos = [["id_modulo", "ordem"]]
    chaves_estrangeiras = [{
        "key": "id_tipo", "tabela": "aulas_tipo"
    }, {
        "key": "id_modulo", "tabela": "modulos"
    }]
    erros = []

    aulas = ler_arquivo_csv("aulas")
    for aula in aulas:
        aula_erro = {
            "data": aula,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=aulas, data=aula, obrigatorios=obrigatorios, unicos_compostos=unicos_compostos, numeros=numeros, unicos=unicos, chaves_estrangeiras=chaves_estrangeiras)
        if erros_validacao:
            aula_erro["erros"].extend(erros_validacao)
            erros.append(aula_erro)

    return erros


def valida_matriculas_status():
    obrigatorios = ["id", "status"]
    numeros = ["id"]
    unicos = ["id", "status"]
    erros = []

    matriculas_status = ler_arquivo_csv("matriculas_status")
    for status in matriculas_status:
        matricula_erro = {
            "data": status,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=matriculas_status, data=status, obrigatorios=obrigatorios, numeros=numeros, unicos=unicos)
        if erros_validacao:
            matricula_erro["erros"].extend(erros_validacao)
            erros.append(matricula_erro)

    return erros


def valida_matriculas():
    obrigatorios = ["id", "valor_pago", "data_matricula", "id_aluno", "id_curso", "id_status"]
    numeros = ["id", "id_aluno", "id_curso", "id_status"]
    datetimes = ["data_matricula", "data_pagamento"]
    unicos = ["id"]
    unicos_compostos = [["id_aluno", "id_curso", "id_status"]]
    chaves_estrangeiras = [{
        "key": "id_aluno", "tabela": "alunos"
    }, {
        "key": "id_curso", "tabela": "cursos"
    }, {
        "key": "id_status", "tabela": "matriculas_status"
    }]
    erros = []

    matriculas = ler_arquivo_csv("matriculas")
    for matricula in matriculas:
        matricula_erro = {
            "data": matricula,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=matriculas, data=matricula, obrigatorios=obrigatorios, unicos_compostos=unicos_compostos, numeros=numeros, datetimes=datetimes, unicos=unicos, chaves_estrangeiras=chaves_estrangeiras)
        if erros_validacao:
            matricula_erro["erros"].extend(erros_validacao)
            erros.append(matricula_erro)
    return erros


def valida_progresso_aulas():
    obrigatorios = ["id", "tempo_assistido", "concluida", "id_aula", "id_matricula"]
    numeros = ["id", "id_aula", "id_matricula"]
    datetimes = ["data_conclusao"]
    unicos = ["id"]
    unicos_compostos = [["id_aula", "id_matricula"]]
    chaves_estrangeiras = [{
        "key": "id_aula", "tabela": "aulas"
    }, {
        "key": "id_matricula", "tabela": "matriculas"
    }]
    erros = []

    progresso_aulas = ler_arquivo_csv("progresso_aulas")
    for progresso in progresso_aulas:
        progresso_erro = {
            "data": progresso,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=progresso_aulas, data=progresso, obrigatorios=obrigatorios, unicos_compostos=unicos_compostos, numeros=numeros, datetimes=datetimes, unicos=unicos, chaves_estrangeiras=chaves_estrangeiras)
        if erros_validacao:
            progresso_erro["erros"].extend(erros_validacao)
            erros.append(progresso_erro)
    return erros


def valida_avaliacoes():
    obrigatorios = ["id", "nota", "data_avaliacao", "comentario", "id_curso", "id_matricula"]
    numeros = ["id", "nota", "id_curso", "id_matricula"]
    datetimes = ["data_avaliacao"]
    unicos = ["id"]
    chaves_estrangeiras = [{
        "key": "id_curso", "tabela": "cursos"
    }, {
        "key": "id_matricula", "tabela": "matriculas"
    }]
    erros = []

    avaliacoes = ler_arquivo_csv("avaliacoes")
    for avaliacao in avaliacoes:
        avaliacao_erro = {
            "data": avaliacao,
            "erros": []
        }

        erros_validacao = valida_dado(lista_existente=avaliacoes, data=avaliacao, obrigatorios=obrigatorios, numeros=numeros, datetimes=datetimes, unicos=unicos, chaves_estrangeiras=chaves_estrangeiras)

        if not avaliacao["nota"] or not (1 <= int(avaliacao["nota"]) <= 5):
            erro_nota = {
                "tipo": "constraint_intervalo_nota",
                "key": "nota"
            }
            erros_validacao.append(erro_nota)

        if erros_validacao:
            avaliacao_erro["erros"].extend(erros_validacao)
            erros.append(avaliacao_erro)

    return erros


def validador_csv():
    erros = {}

    erros_alunos = valida_alunos()
    if len(erros_alunos) > 0:
        erros["alunos"] = erros_alunos

    erros_especialidades = valida_especialidades()
    if len(erros_especialidades) > 0:
        erros["especialidades"] = erros_especialidades

    erros_instrutores = valida_instrutores()
    if len(erros_instrutores) > 0:
        erros["instrutores"] = erros_instrutores

    erros_especialidades_instrutores = valida_especialidades_instrutores()
    if len(erros_especialidades_instrutores) > 0:
        erros["especialidades_instrutores"] = erros_especialidades_instrutores

    erros_categorias = valida_categorias()
    if len(erros_categorias) > 0:
        erros["categorias"] = erros_categorias

    erros_cursos_nivel = valida_cursos_nivel()
    if len(erros_cursos_nivel) > 0:
        erros["cursos_nivel"] = erros_cursos_nivel

    erros_cursos = valida_cursos()
    if len(erros_cursos) > 0:
        erros["cursos"] = erros_cursos

    erros_modulos = valida_modulos()
    if len(erros_modulos) > 0:
        erros["modulos"] = erros_modulos

    erros_aulas_tipo = valida_aulas_tipo()
    if len(erros_aulas_tipo) > 0:
        erros["aulas_tipo"] = erros_aulas_tipo

    erros_aulas = valida_aulas()
    if len(erros_aulas) > 0:
        erros["aulas"] = erros_aulas

    erros_matriculas_status = valida_matriculas_status()
    if len(erros_matriculas_status) > 0:
        erros["matriculas_status"] = erros_matriculas_status

    erros_matriculas = valida_matriculas()
    if len(erros_matriculas) > 0:
        erros["matriculas"] = erros_matriculas

    erros_progresso_aulas = valida_progresso_aulas()
    if len(erros_progresso_aulas) > 0:
        erros["progresso_aulas"] = erros_progresso_aulas

    erros_avaliacoes = valida_avaliacoes()
    if len(erros_avaliacoes) > 0:
        erros["avaliacoes"] = erros_avaliacoes

    return erros


def gera_relatorio_erros(erros):
    arquivos_analisados = erros.keys()

    if len(arquivos_analisados) == 0:
        print("Nenhum erro encontrado.\n")
        return

    with open("./relatorio_erros.md", mode="w", newline="", encoding="utf-8") as arquivo:
        write = arquivo.write
        write("# Relatório de Erros\n")

        for arquivo in arquivos_analisados:
            write(f"\n## Arquivo: {str(arquivo).upper()}\n")

            if len(erros[arquivo]) == 0:
                write("Nenhum erro encontrado.\n\n")
                continue

            write("### Erros Encontrados: \n\n")
            write("| Tipo de Erro | Campo(s) | Valor(es) | \n")
            write("| :-- | :-- | :-- | \n")

            for obj in erros[arquivo]:
                for erro in obj["erros"]:
                    if erro.get("key"):
                        write(f"| {erro['tipo']} | {erro['key']} | {obj['data'][erro['key']]} | \n")
                    elif erro.get("keys"):
                        write(f"| {erro['tipo']} | {', '.join(erro['keys'])} | {', '.join(obj['data'][key] for key in erro['keys'])} | \n")

    print("Relatório de erros gerado em './relatorio_erros.md'.")


if __name__ == "__main__":
    erros = validador_csv()
    gera_relatorio_erros(erros)
