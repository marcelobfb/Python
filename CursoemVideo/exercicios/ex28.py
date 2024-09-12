import random
n1=int(input('Qual número o computador está pensando de 1 a 5? '))
n2=(random.randint(1,5))
if n1==n2:
    print('Parabéns você acertou!')
else:
    print('Tente novamente...')
print('Eu estava pensando em {}.'.format(n2))