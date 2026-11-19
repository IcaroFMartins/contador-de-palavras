from pathlib import Path
from text_analyzer import estatisticas


def ler_arquivo(caminho):
    arquivo = Path(caminho)

    if not arquivo.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    return arquivo.read_text(encoding="utf-8")


def main():
    print("=" * 30)
    print("Contador de Palavras")
    print("=" * 30)

    caminho = input("Digite o caminho do arquivo de texto: ")

    try:
        texto = ler_arquivo(caminho)
        resultado = estatisticas(texto)

        print(f"\nTotal de palavras: {resultado['total_palavras']}")
        print(f"Palavras únicas: {resultado['palavras_unicas']}")
        print("\nPalavras mais frequentes:")

        for palavra, quantidade in resultado["mais_frequentes"]:
            print(f"{palavra}: {quantidade}")

    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()