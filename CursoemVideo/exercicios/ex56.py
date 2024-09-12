import math

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20=0
for c in range(1, 5):
    print('----- {} Pessoa -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20+=1
mediaidade = somaidade / 4
print('-' * 20)
print('A média de idade do grupo é de {}.'.format(mediaidade))
print('-' * 20)
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho.capitalize(), maioridadehomem))
print('-' * 20)
print('O total de mulher com menos de 20 anos é {}.'.format(mulher20))
