n1=float(input('Qual o seu salário? R$'))
n2=n1*0.10+n1
n3=n1*0.15+n1
if n1>1250:
    print('Seu salário recebeu um aumento de 10%, seu novo salário é de R${:.2f}.'.format(n2))
if n1<=1250:
    print('Seu salário recebeu um aumento de 15%, seu novo salário é de R${:.2f}.'.format(n3))