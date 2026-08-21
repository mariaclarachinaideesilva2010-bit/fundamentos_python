# Autor: Maria Clara 
# Projeto: Utilizando IF/ELIF/ELSE
# Operadores de comparação
# == igual
# != diferente


# Definição das variáveis
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1+nota2)/2
print(f'A média é: {media:.2f}') # :.2f formata para 2 casas decimais

# Estrutura condicional
# Se a média for >= 7 então Aluno Aprovado
# Se a média for < que 7 então Aluno Reprovado
if media >= 7:
    # \n serve para pular uma linha
    print('Aluno Aprovado! \n😍')
else:
    print('Aluno Reprovado! \n😒')    