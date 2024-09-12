import math
lista=[]
for c in range(1,6):
    n1=float(input('Qual o peso da {} pessoa? '.format(c)))
    lista+=[n1]
print('O maior peso foi {}.'.format(max(lista)))
print('O menor peso foi {}.'.format(min(lista)))
print(lista)