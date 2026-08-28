# Autor: Maria Clara
# Projeto: Contratado por uma pizzaria 

print('CARDÁPIO')
print('1 - Calabresa')
print('2 - Muçarela')
print('3 - Frango')

pizza = input('Escolha uma pizza: ')

print('Você escolheu: ', pizza)

mais = input('Deseja mais algum item?(sim ou não) ')

if mais == 'sim':
    pizza2 = input('Digite o próximo item: ')
    print('Você também escolheu:', pizza2)

else:
    print('Pedido finalizado!')