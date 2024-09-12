n1=float(input('Qual a distância de seu destino? '))
n2=n1*0.50
n3=n1*0.45
if n1>200:
    print('A passagem será de R${}.'.format(n3))
else:
    print('A passagem será de R${}.'.format(n2))