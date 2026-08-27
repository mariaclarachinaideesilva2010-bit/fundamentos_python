# Autor: Maria Clara
# Projeto: Fatorial

# A expressão completa fica assim:
# 6! = 6 × 5 × 4 × 3 × 2 × 1 = 720 

numero = int(input('Digite a fatorial desejada: '))
fatorial = 1

for i in range(1,numero+1):
    # calculo da fatorial
    fatorial=fatorial*i

    # print do resultado
    print(f' Fatorial: {fatorial}')