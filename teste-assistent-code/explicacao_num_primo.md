# Explicação técnica do código `eh_primo`

O arquivo `num_primos.py` contém a função `eh_primo(n)` e um bloco `main()` para testar alguns valores.

## Estrutura limpa do código

- `eh_primo(n: int) -> bool` é uma função pequena e objetiva.
- `main()` centraliza o exemplo de execução e deixa a função de verificação separada.
- O uso de nomes claros como `divisor`, `números` e `status` melhora a legibilidade.

## Como `eh_primo` determina primalidade

1. Retorna `False` para `n <= 1`, porque esses valores não são primos.
2. Retorna `True` para `n == 2` ou `n == 3`.
3. Retorna `False` se `n` for divisível por 2 ou por 3.

## Otimização com padrão 6k ± 1

Depois das verificações iniciais, a função testa apenas divisores do tipo `6k - 1` e `6k + 1`:

- `divisor = 5`
- `while divisor * divisor <= n:`
- `n % divisor == 0` ou `n % (divisor + 2) == 0`
- `divisor += 6`

Isso reduz a quantidade de testes necessários e mantém a lógica correta.

## Por que `divisor * divisor <= n` é suficiente

Se `n` possui um divisor maior que sua raiz quadrada, então já existe um divisor menor que a raiz quadrada. Por isso, não é preciso testar valores além de `sqrt(n)`.

## Separação de responsabilidades

- A função `eh_primo` trata apenas da lógica de primalidade.
- O bloco `main()` trata apenas da demonstração e da impressão dos resultados.

## Exemplo de saída

O código imprime algo como:

- `1 -> não primo`
- `2 -> primo`
- `3 -> primo`
- `4 -> não primo`
- `17 -> primo`

Essa organização torna o código mais fácil de manter e entender.
