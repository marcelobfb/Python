import termcolor
n1=int(input('Qual a velocidade do carro? '))
n2=(n1-80)*7
if n1>80:
    print('Você foi multado por está a {:.2f}km/h, a velocidade maxima permitida é de 80km/h.'.format(n1))
    print('A multa é de R${:.2f}.'.format(n2))
else:
    print('Você está dentro da velocidade permitida.')
