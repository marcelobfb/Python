n1 = n2 = n3 = n4 = 0
while n1 != 999:
    n1 = int(input('Digite um número (999 para parar): '))
    n2 += 1
    n3 = n1
    n4 += n3
print('Foram pedidos {} números e a soma deles é {}.'.format(n2 - 1, n4 - 999))
