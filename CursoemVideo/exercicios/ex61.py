n1 = int(input('Qual o primeiro termo: '))
n2 = int(input('Qual o segundo termo: '))
termo = n1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' → ')
    termo += n2
    cont += 1
print('END')
