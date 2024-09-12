n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))
if n1 > n2 > n3:
    print('O maior número é {} e o menor é {}.'.format(n1, n3))
if n2 > n3 > n1:
    print('O maior número é {} e o menor é {}.'.format(n2, n1))
if n3 > n1 > n2:
    print('O maior número é {} e o menor é {}.'.format(n3, n2))
if n1 > n3 > n2:
    print('O maior número é {} e o menor é {}.'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior número é {} e o menor é {}.'.format(n2, n3))
if n3 > n2 > n1:
    print('O maior número é {} e menor é {}.'.format(n3, n1))
