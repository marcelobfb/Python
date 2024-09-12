n1=str(input('Digite uma frase: ')).replace(' ','').upper()
n2=(n1[::-1]).upper()
if n1==n2:
    print('A frase é um políndromo.')
else:
    print('A frase não é um políndromo.')
print('O inverso de {} é {}.'.format(n1,n2))
