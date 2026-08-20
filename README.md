# 🐍 Conceitos Básicos de Python

Este README apresenta alguns dos principais conceitos iniciais da linguagem **Python**, incluindo:

* Variáveis
* `print()`
* F-strings
* `if`
* `elif`
* `else`

---

## 📌 1. Variáveis

Uma **variável** é um espaço utilizado para armazenar uma informação que pode ser usada posteriormente no programa.

Em Python, não é necessário declarar o tipo da variável antes de utilizá-la.

### Exemplo:

```python
nome = "Maria"
idade = 15
altura = 1.65
```

Nesse exemplo:

* `nome` armazena um texto (`str`);
* `idade` armazena um número inteiro (`int`);
* `altura` armazena um número decimal (`float`).

Podemos utilizar uma variável em outras partes do código:

```python
nome = "Maria"
print(nome)
```

**Saída:**

```text
Maria
```

### Tipos comuns de variáveis

| Tipo    | Exemplo | Descrição           |
| ------- | ------- | ------------------- |
| `str`   | `"Olá"` | Texto               |
| `int`   | `15`    | Número inteiro      |
| `float` | `1.65`  | Número decimal      |
| `bool`  | `True`  | Verdadeiro ou falso |

---

## 🖨️ 2. `print()`

A função `print()` é utilizada para **mostrar informações na tela**.

### Exemplo:

```python
print("Olá, mundo!")
```

**Saída:**

```text
Olá, mundo!
```

Também podemos imprimir variáveis:

```python
nome = "Maria"
idade = 15

print(nome)
print(idade)
```

**Saída:**

```text
Maria
15
```

É possível imprimir várias informações no mesmo `print()`:

```python
nome = "Maria"
idade = 15

print(nome, idade)
```

**Saída:**

```text
Maria 15
```

---

## ✨ 3. F-string

As **f-strings** são uma maneira simples de colocar variáveis dentro de textos.

Para utilizar uma f-string, colocamos a letra `f` antes das aspas e usamos `{}` para inserir as variáveis.

### Exemplo:

```python
nome = "Maria"
idade = 15

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

**Saída:**

```text
Meu nome é Maria e tenho 15 anos.
```

Sem f-string, seria necessário juntar as informações de outra maneira. Por isso, f-strings tornam o código mais fácil de ler.

### Outro exemplo:

```python
produto = "Notebook"
preco = 2500

print(f"O {produto} custa R${preco}.")
```

**Saída:**

```text
O Notebook custa R$2500.
```

---

# 🔀 4. `if`

O `if` é utilizado para criar uma **condição**.

Ele significa basicamente:

> **"Se isso acontecer, faça isso."**

### Exemplo:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

Como `idade` é igual a 18, a condição `idade >= 18` é verdadeira e o `print()` será executado.

### Operadores de comparação

| Operador | Significado    |
| -------- | -------------- |
| `==`     | Igual          |
| `!=`     | Diferente      |
| `>`      | Maior que      |
| `<`      | Menor que      |
| `>=`     | Maior ou igual |
| `<=`     | Menor ou igual |

⚠️ **Atenção:** `=` e `==` são diferentes.

```python
idade = 18
```

O `=` atribui um valor à variável.

```python
idade == 18
```

O `==` verifica se os valores são iguais.

---

# 🔄 5. `elif`

O `elif` significa **"else if"** e é utilizado quando queremos verificar uma **segunda ou outra condição**, caso o `if` não seja verdadeiro.

### Exemplo:

```python
nota = 7

if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprovado!")
```

Como a nota é `7`, a primeira condição é falsa, então o Python verifica o `elif`.

**Saída:**

```text
Aprovado!
```

Podemos utilizar vários `elif`:

```python
nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Muito bom!")
elif nota >= 5:
    print("Regular!")
```

**Saída:**

```text
Muito bom!
```

---

# ❌ 6. `else`

O `else` é utilizado quando **nenhuma das condições anteriores é verdadeira**.

Ele significa:

> **"Caso contrário, faça isso."**

### Exemplo:

```python
idade = 15

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

Como `15` não é maior ou igual a `18`, o `else` será executado.

**Saída:**

```text
Menor de idade.
```

---

# 🧩 7. Usando `if`, `elif` e `else` juntos

Podemos combinar os três para criar diferentes possibilidades.

### Exemplo:

```python
nota = 7

if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
```

O programa funciona da seguinte maneira:

1. Verifica se a nota é maior ou igual a `9`.
2. Se não for, verifica se é maior ou igual a `6`.
3. Se nenhuma das duas condições for verdadeira, executa o `else`.

---

# 🚀 8. Exemplo completo

Podemos juntar todos os conceitos aprendidos:

```python
nome = "Maria"
idade = 15
nota = 8

print(f"Aluno(a): {nome}")
print(f"Idade: {idade}")
print(f"Nota: {nota}")

if nota >= 9:
    print("Resultado: Excelente!")
elif nota >= 6:
    print("Resultado: Aprovado!")
else:
    print("Resultado: Reprovado!")
```

**Saída:**

```text
Aluno(a): Maria
Idade: 15
Nota: 8
Resultado: Aprovado!
```

---

## 📚 Resumo

| Conceito      | Função                                            |
| ------------- | ------------------------------------------------- |
| **Variável**  | Armazena informações                              |
| **`print()`** | Mostra informações na tela                        |
| **F-string**  | Facilita a inserção de variáveis em textos        |
| **`if`**      | Verifica uma condição                             |
| **`elif`**    | Verifica outra condição                           |
| **`else`**    | Executa quando as condições anteriores são falsas |

### 💡 Estrutura básica de condições

```python
if condição:
    # código executado se for verdadeiro
elif outra_condição:
    # código executado se a segunda condição for verdadeira
else:
    # código executado se nenhuma condição for verdadeira
```

---

## 🎯 Conclusão

Esses conceitos são fundamentais para quem está começando a programar em Python. Com **variáveis**, podemos armazenar informações; com `print()`, podemos exibi-las; com **f-strings**, podemos criar mensagens personalizadas; e com `if`, `elif` e `else`, podemos fazer o programa **tomar decisões de acordo com diferentes situações**.

🐍 Com esses fundamentos, já é possível começar a criar programas simples e evoluir para conceitos mais avançados de Python.
