import math
n1=int(input('Escolha um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é {}.'.format(n1,bin(n1)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}.'.format(n1,oct(n1)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n1,hex(n1)[2:]))
else:
    print('Número invalido, tente novamente.')