primeiro=int(input('Quantos termos você deseja mostrar: '))
termo=3
n1=0
n2=1
n3=n1+n2
print('{} → {}'.format(n1,n2),end=' → ')
while termo<=primeiro:
    n3=n1+n2
    print('{}'.format(n3),end=' → ')
    n1=n2
    n2=n3
    termo+=1
print('Fim')