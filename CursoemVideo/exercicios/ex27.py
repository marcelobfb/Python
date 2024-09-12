n1=str(input('Qual o seu nome: ')).strip().split()
print('Seu primeiro nome é {}.'.format(n1.pop(0)))
print('Seu último nome é {}.'.format(n1.pop()))