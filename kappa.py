from nltk import agreement
import pandas as pd

def calcular_kappa(df, colunas):
    """
    Calcula o Kappa usando as funções kappa() e multi_kappa da biblioteca nltk.

    Parâmetros:
    df (pandas.DataFrame): DataFrame original
    colunas (list): Lista com os nomes das colunas dos anotadores

    Retorna:
    float: Kappa
    """
    dados_anotados = []

    # Itera sobre cada coluna de anotador
    for idx_anotador, coluna in enumerate(colunas):
        dados_anotador = [
            [idx_anotador, str(indice), str(valor)]
            for indice, valor in enumerate(df[coluna])
        ]
        dados_anotados.extend(dados_anotador)

    # Cria tarefa de anotação
    anotacao = agreement.AnnotationTask(data=dados_anotados)

    # Calcula Cohen's Kappa para 2 anotadores
    if len(colunas) == 2:
        kappa = anotacao.kappa()
    # Calcula Fleiss' Kappa para mais de 2 anotadores
    else:
        kappa = anotacao.multi_kappa()

    return kappa
