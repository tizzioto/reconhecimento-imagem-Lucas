# Explicação dos Erros no Código

## Erros Encontrados

### 1. **Erro na linha 4: Falta de aspas na string de input**
```python
item1 = float(input(Preço do item 1? ))  # ❌ ERRO
```
**Problema:** A string `"Preço do item 1?"` não tem aspas.
**Solução:** Adicionar aspas duplas ao redor do texto.
```python
item1 = float(input("Preço do item 1? "))  # ✅ CORRETO
```

---

### 2. **Erro na linha 23: desconto_cupom é string, mas usado como número**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```
**Problema:** `input()` retorna uma string. Na linha 28 e 35, tenta-se usar esse valor em operações matemáticas (`desconto_cupom / 100` e `desconto_cupom > 0`), o que causa erro.
**Solução:** Converter a entrada para número inteiro ou float.
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

### 3. **Erro na linha 29: Falta de 'f' antes da string formatada**
```python
print(" Item 2:        R$ {total_item2:.2f}")  # ❌ ERRO
```
**Problema:** A string não tem o prefixo `f`, então as chaves `{}` são tratadas como texto literal, não como interpolação.
**Solução:** Adicionar `f` antes das aspas.
```python
print(f" Item 2:        R$ {total_item2:.2f}")  # ✅ CORRETO
```

---

### 4. **Erro na linha 35: Indentação incorreta**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```
**Problema:** O comando `print` não está indentado dentro do bloco `if`.
**Solução:** Adicionar 4 espaços (ou 1 tab) antes do `print`.
```python
if desconto_cupom > 0: 
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # ✅ CORRETO
```

---

## Resumo dos Erros
| Linha | Tipo | Descrição |
|-------|------|-----------|
| 4 | Sintaxe | Falta de aspas na string |
| 23 | Tipo de Dado | String usada em operação matemática |
| 29 | Sintaxe | Falta de `f` na f-string |
| 35 | Indentação | `print` não indentado dentro do `if` |
