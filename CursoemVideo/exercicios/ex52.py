import math

n1 = int(input('Digite um número inteiro: '))
co=0
for c in range(1,n1+1):
    if n1%c==0:
        print('\033[32m',end=' ')
        co+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO numero {} foi dividido {} vezes.'.format(n1,co))
if co==2:
    print('O número é primo.')
else:
    print('O numero não é primo.')