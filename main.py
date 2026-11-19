import sys
from pathlib import Path

from text_analyzer import estatisticas, exportar_csv


def ler_arquivo(caminho):
    arquivo = Path(caminho)

    if not arquivo.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    return arquivo.read_text(encoding="utf-8")


def ler_texto_do_terminal():
    print("Cole ou digite o texto. Pressione Enter duas vezes para finalizar:\n")

    linhas = []

    while True:
        linha = input()

        if linha == "":
            break

        linhas.append(linha)

    return "\n".join(linhas)


def mostrar_resultado(resultado):
    print(f"\nTotal de palavras: {resultado['total_palavras']}")
    print(f"Palavras únicas: {resultado['palavras_unicas']}")
    print("\nPalavras mais frequentes:")

    for palavra, quantidade in resultado["mais_frequentes"]:
        print(f"{palavra}: {quantidade}")


def main():
    print("Contador de Palavras")
    print("=" * 30)
    print("1 - Analisar arquivo de texto")
    print("2 - Analisar texto colado no terminal")

    opcao = input("\nEscolha uma opção: ").strip()

    try:
        if opcao == "1":
            caminho = input("Digite o caminho do arquivo de texto: ")
            texto = ler_arquivo(caminho)
        elif opcao == "2":
            texto = ler_texto_do_terminal()
        else:
            print("Opção inválida.")
            sys.exit(1)

        if not texto.strip():
            print("Nenhum texto foi informado.")
            sys.exit(1)

        resultado = estatisticas(texto, ignorar_comuns=True)
        mostrar_resultado(resultado)

        salvar = input("\nSalvar relatório em CSV? (s/n): ").strip().lower()

        if salvar == "s":
            caminho_csv = exportar_csv(resultado["contador"])
            print(f"Relatório salvo em: {caminho_csv}")

    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()