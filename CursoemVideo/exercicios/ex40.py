n1=float(input('Qual foi a nota da sua primeira avaliação? '))
n2=float(input('Qual foi a nota da sua segunda avaliação? '))
n3=(n1+n2)/2
if n3>=7.0:
    print('Parabéns você foi aprovado com média {}.'.format(n3))
elif n3<6.9 and n3>=5.0:
    print('Você esta de recuperação com média {}.'.format(n3))
elif n3<5.0:
    print('Você esta reprovado com média {}.'.format(n3))