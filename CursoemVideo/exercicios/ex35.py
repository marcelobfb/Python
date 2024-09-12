n1=float(input('Qual o comprimento da primeira reta? '))
n2=float(input('Qual o comprimento da segunda reta? '))
n3=float(input('Qual o comprimento da terceira reta? '))
if (n2-n3)<n1<n2+n3 and (n1-n3)<n2<n1+n3 and (n1-n2)<n3<n1+n2:
    print('É possivel formar um triangulo.')
else:
    print('Não é possivel formar um triangulo.')