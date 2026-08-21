# Autor: Maria Clara
# Projeto: Motorista if/else | and | variáveis

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
carteira = True


# Estrura condicional
# and -> todas as condições tem que ser verdadeiras
if idade >= 18 and carteira:
    print('Pode dirigir')
else:
    print('Não pode dirigir')