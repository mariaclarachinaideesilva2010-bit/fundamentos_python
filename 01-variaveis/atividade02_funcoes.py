# Autor: Maria Clara
# Projeto: Trabalhando com funções

'''
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor'))
soma = valor1+valor2
subtracao = valor1-valor2
multiplicacao = valor1*valor2
divisao = valor1/valor2
print(f'O valor da soma é: {soma}')
print(f'O valor da soma é: {subtracao}')
print(f'O valor da soma é: {multiplicacao}')
print(f'O valor da soma é: {divisao}')
'''

# Função para realizar os cálculos
def calculadora(valor1,valor2):
    soma = valor1+valor2
    subtracao = valor1-valor2
    multiplicacao = valor1*valor2
    divisao = valor1/valor2

    print(f'O valor da soma é: {soma}')
    print(f'O valor da subtração é: {subtracao}')
    print(f'O valor da multiplicação é: {multiplicacao}')
    print(f'O valor da divisão é: {divisao}')

# Entrada de dados 
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
# Chamada da função
calculadora(valor1,valor2)