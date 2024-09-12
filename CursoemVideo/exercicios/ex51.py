import math
n1=int(input('Primeiro termo: '))
n2=int(input('Segundo termo: '))
n3=n1+(10-1)*n2
for c in range(n1,n3+n2,n2):
    print('{}'.format(c), end=' → ')
print('FIM')