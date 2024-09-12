n1=float(input('Qual o seu peso? (kg) '))
n2=float(input('Qual sua altura? (m) '))
imc=n1/(n2*n2)
if imc<18.5:
    print('Você está abaixo do peso.')
elif imc<25 and imc>=18.5:
    print('Voce esta no peso ideal')
elif imc>=25 and imc<30:
    print('Voce esta com sobrepeso.')
elif imc>=30 and imc<40:
    print('Voce esta com obesidade.')
else:
    print('Voce esta com obesidade morbida.')
print('Seu imc é de {:.1f}.'.format(imc))