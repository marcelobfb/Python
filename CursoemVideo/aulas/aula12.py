n1=str(input('Qual é seu nome? ')).upper()
if n1=='MARCELO':
    print('Que nome bonito.')
elif n1=='ANA':
    print('Que nome bom')
else:
    print('Bom dia')
print('Tenha uma boa semana tb {}.'.format(n1.capitalize()))