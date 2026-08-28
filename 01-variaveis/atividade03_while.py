# Autor: Maria Clara
# Projeto: Loop While

comando='' 

# == significa igual
# != significa diferente

while comando != 'sim':
    comando=input('Digite sim ou não: ')
    print(f'você digitou {comando}')