import math
n1=float(input('Qual o comprimento do cateto oposto?'))
n2=float(input('Qual o comprimento do cateto adjacente?'))
n3=math.hypot(n1,n2)
print('Um triangulo com comprimento do cateto oposto de {}cm e {}cm de cateto adjacente, tem {:.2f}cm de comprimento da hipotenusa.'.format(n1,n2,n3))