n1 = int(input('Qual o primeiro termo: '))
n2 = int(input('Qual o segundo termo: '))
termo = n1
cont = 1
total=0
n3=10
while n3!=0:
    total+=n3
    while cont <= total:
        print('{}'.format(termo), end=' → ')
        termo += n2
        cont += 1
    print('Fim')
    n3 = int(input('Quantos termos deseja mostrar a mais? '))
print('Fim')
