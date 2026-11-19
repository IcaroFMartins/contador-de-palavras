import string
from collections import Counter


def limpar_texto(texto):
    texto = texto.lower()

    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, " ")

    return texto


def contar_palavras(texto):
    palavras = limpar_texto(texto).split()
    return Counter(palavras)


def palavras_mais_frequentes(contador, quantidade=10):
    return contador.most_common(quantidade)


def estatisticas(texto):
    contador = contar_palavras(texto)
    total_palavras = sum(contador.values())
    palavras_unicas = len(contador)

    return {
        "total_palavras": total_palavras,
        "palavras_unicas": palavras_unicas,
        "mais_frequentes": palavras_mais_frequentes(contador),
    }