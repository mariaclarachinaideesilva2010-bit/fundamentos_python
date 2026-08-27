# Autor: Maria Clara
# Projeto: Desafio juros simples


c = float(input('Digite a capital inicial: '))
i = float(input('Digite a taxa ( em decimal)'))
t = int(input('Digite o tempo: '))

j=c * i * t
montante= j + c

print(f'a taxa é {j}. E o montante é: {montante}')