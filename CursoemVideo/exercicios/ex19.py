import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1,n2,n3,n4]
print('O aluno escolhido foi {}.'.format(random.choice(lista)))