from time import sleep
print('-'*5,'Cálculadora do Celov','-'*5)
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
n3=0
while n3!=5:
    n3=int(input('''Menu interativo
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos digitos
    [5] Sair do programa
    Digite o código: '''))
    if n3==1:
        print('{}+{}={}'.format(n1,n2,(n1+n2)))
        sleep(1)
    if n3==2:
        print('{}x{}={}'.format(n1,n2,(n1*n2)))
        sleep(1)
    if n3==3:
        if n1>n2:
            print('{}>{}'.format(n1,n2))
            sleep(1)
        if n2>n1:
            print('{}>{}'.format(n2,n1))
            sleep(1)
        if n1>=n2:
            print('Os valores são iguais.')
            sleep(1)
    if n3==4:
       n1 = int(input('Digite o primeiro valor: '))
       n2 = int(input('Digite o segundo valor: '))

