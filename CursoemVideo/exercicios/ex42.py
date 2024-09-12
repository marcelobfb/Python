n1=float(input('Qual a primeira medida? '))
n2=float(input('Qual a segunda medida? '))
n3=float(input('Qual a terceira medida? '))
if (n2-n3)<n1<n2+n3 and (n1-n3)<n2<n1+n3 and (n1-n2)<n3<n1+n2:
    print('É possivel formar um triangulo.')
    if n1==n2==n3:
        print('O triangulo é equilátero.')
    if n1==n2!=n3 or n2==n3!=n1 or n1==n3!=n2:
        print('O triangulo é isosceles.')
    if n1!=n2!=n3!=n1:
        print('O triangulo é escaleno.')
else:
    print('Não é possivel formar um triangulo.')