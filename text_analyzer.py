import csv
import string
from collections import Counter
from pathlib import Path


PALAVRAS_IGNORADAS = {
    "a", "o", "as", "os", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na",
    "nos", "nas", "e", "ou", "que", "para", "por", "com",
    "é", "são", "ser", "ao", "à", "às", "seu", "sua",
}


def limpar_texto(texto):
    texto = texto.lower()

    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, " ")

    return texto


def contar_palavras(texto, ignorar_comuns=True):
    palavras = limpar_texto(texto).split()

    if ignorar_comuns:
        palavras = [
            palavra
            for palavra in palavras
            if palavra not in PALAVRAS_IGNORADAS
        ]

    return Counter(palavras)


def palavras_mais_frequentes(contador, quantidade=10):
    return contador.most_common(quantidade)


def estatisticas(texto, ignorar_comuns=True):
    contador = contar_palavras(texto, ignorar_comuns=ignorar_comuns)

    return {
        "contador": contador,
        "total_palavras": sum(contador.values()),
        "palavras_unicas": len(contador),
        "mais_frequentes": palavras_mais_frequentes(contador),
    }


def exportar_csv(contador, caminho="relatorio-palavras.csv"):
    with Path(caminho).open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["palavra", "frequencia"])

        for palavra, frequencia in contador.most_common():
            escritor.writerow([palavra, frequencia])

    return caminho