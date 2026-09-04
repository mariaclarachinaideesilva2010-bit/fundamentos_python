# Autor: Maria Clara 
# Projeto: Trabalhando com funções

# Estrutura sem função
'''
base = float(input('Valor da base: '))
altura = float(input('Valor da altura: '))
area_triangulo = (base*altura)/2
print(f'A área do triângulo é: {area_triangulo:.2f}')
'''

# Estrura com função
def calc_area_triangulo (b,a):
    area = (b*a)/2
    return area

# Entrada de dados
base = float(input('Valor da base: '))
altura = float(input('Valor da altura: '))
resultado = calc_area_triangulo(base, altura)
print(f'A área do triângulo é: {resultado:.2f}')