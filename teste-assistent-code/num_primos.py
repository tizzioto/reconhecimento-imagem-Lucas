def eh_primo(n: int) -> bool:
    """Verifica se um número inteiro é primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


def main() -> None:
    números = [1, 2, 3, 4, 16, 17, 19, 20, 23, 24]
    for número in números:
        status = "primo" if eh_primo(número) else "não primo"
        print(f"{número} -> {status}")


if __name__ == "__main__":
    main()
