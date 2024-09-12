n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
n3= (n1+n2)/2
if n3>=6.0:
    print('Você passou, parabéns!')
else:
    print('Você foi reprovado.')
print('Sua média é {:.2f}.'.format(n3))