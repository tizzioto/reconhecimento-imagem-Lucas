from typing import List, Tuple


def calcular_estatisticas(valores: List[float]) -> Tuple[float, float, float, float]:
    """Retorna a soma, a média, o maior e o menor valor da lista."""
    if not valores:
        raise ValueError("A lista de valores não pode ser vazia.")

    total = sum(valores)
    media = total / len(valores)
    maior = max(valores)
    menor = min(valores)

    return total, media, maior, menor

def main() -> None:
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numeros)

    print("total:", total)
    print("media:", media)
    print("maior:", maior)
    print("menor:", menor)


if __name__ == "__main__":
    main()