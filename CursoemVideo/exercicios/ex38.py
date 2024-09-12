n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))
if n1>n2:
    print('{} é o maior número.'.format(n1))
elif n2>n1:
    print('{} é o maior número.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')