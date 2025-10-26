import re

from utils import ler_arquivo_csv, validar_email

def valida_campos_obrigatorios(data, keys):
    erros = []

    for key in keys:
        if not data[key]:
            erro = {
                "tipo": "campo_obrigatorio",
                "key": key
            }
            erros.append(erro)
    return erros

def valida_campos_inteiros(data, keys):
    erros = []

    for key in keys:
        try:
            int(data[key])
        except (ValueError, TypeError):
            erro = {
                "tipo": "campo_inteiro",
                "key": key
            }
            erros.append(erro)
    return erros

def valida_campos_datas(data, keys):
    erros = []

    for key in keys:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", data[key]):
            erro = {
                "tipo": "formato_data_invalido",
                "key": key
            }
            erros.append(erro)
    return erros

def valida_campos_unicos(lista, data, keys):
    erros = []

    for key in keys:
        values = [item[key] for item in lista if item[key] == data[key]]

        if data[key] and len(values) > 0:
            erro = {
                "tipo": "campo_unico",
                "key": key
            }
            erros.append(erro)
    return erros

def valida_campos_chaves_estrangeiras(data, chaves_estrangeiras):
    erros = []

    for chave in chaves_estrangeiras:
        tabela = chave["tabela"]
        key = chave["key"]

        registros = ler_arquivo_csv(tabela)
        valores_tabela = [registro["id"] for registro in registros]

        if data[key] and data[key] not in valores_tabela:
            erro = {
                "tipo": "chave_estrangeira_invalida",
                "key": key,
                "tabela": tabela
            }
            erros.append(erro)
    return erros

def valida_campos_datetimes(data, keys):
    erros = []

    for key in keys:
        if len(data[key]) > 0 and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z?$", data[key]):
            erro = {
                "tipo": "formato_datetime_invalido",
                "key": key
            }
            erros.append(erro)
    return erros


def valida_campos_emails(data, keys):
    erros = []

    for key in keys:
        if not validar_email(data[key]):
            erro = {
                "tipo": "formato_email_invalido",
                "key": key
            }
            erros.append(erro)
    return erros


def valida_dado(data, obrigatorios=[], numeros=[], datas=[], emails=[], unicos=[], chaves_estrangeiras=[], datetimes=[], lista_existente=[]):
    erros = []

    erros_campos_obrigatorios = valida_campos_obrigatorios(data, obrigatorios)
    erros.extend(erros_campos_obrigatorios)

    erros_campos_inteiros = valida_campos_inteiros(data, numeros)
    erros.extend(erros_campos_inteiros)

    erros_campos_datas = valida_campos_datas(data, datas)
    erros.extend(erros_campos_datas)

    erros_campos_emails = valida_campos_emails(data, emails)
    erros.extend(erros_campos_emails)

    erros_campos_datetimes = valida_campos_datetimes(data, datetimes)
    erros.extend(erros_campos_datetimes)

    erros_campos_unicos = valida_campos_unicos(lista_existente, data, unicos)
    erros.extend(erros_campos_unicos)

    erros_chaves_estrangeiras = valida_campos_chaves_estrangeiras(data, chaves_estrangeiras)
    erros.extend(erros_chaves_estrangeiras)

    return erros