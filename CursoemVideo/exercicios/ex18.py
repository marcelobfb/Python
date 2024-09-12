import math
n1=float(input('Qual é o ângulo? '))
seno=math.sin(math.radians(n1))
cosseno=math.cos(math.radians(n1))
tangente=math.tan(math.radians(n1))
print(' O seno de {} é {:.2f}.\n O cosseno é {:.2f}. \n A tangente é {:.2f}.'.format(n1,seno,cosseno,tangente))