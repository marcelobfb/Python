cont = 1
n=0
s=0
while True:
    n=float(input('digite um numero: '))
    if n==999:
        break
    cont+=1
    s+=n
#print('A soma é {}.'.format(s))
print(f'a soma vale {s:.3}.')
print('Acabou')
