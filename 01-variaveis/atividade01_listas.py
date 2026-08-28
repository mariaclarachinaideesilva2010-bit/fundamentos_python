# Autor: Maria Clara
# Projeto: Listas

# lista de frutas com 5 unidades
#            0       1        2        3       4
frutas = ['banana','maçã','abacaxi','goiaba','kiwi']
print(frutas)

# Adicionar um item na lista
frutas.append('laranja')
print(frutas)

# Alterar o conteúdo de uma posição
# Mudar a fruta: kiwi para morango
frutas[4]='morango'
print(frutas)

# Deletar um item por posição
# Excluir a maçã
del frutas[1]
print(frutas)

# Inserir uma nova fruta na posição 1
frutas.insert(1,'mamão')
print(frutas)

# Ordena a lista
frutas.sort()
print(frutas)