n1=int(input('Um valor:'))
n2=int(input('Outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
c=n1%n2
print('A soma vale {}, a multiplicação vale {}, a divisão vale {:.2f}!'.format(s,m,d), end=' ')
print(f'A divisão inteira vale {di}, a potencia vale {e} ')