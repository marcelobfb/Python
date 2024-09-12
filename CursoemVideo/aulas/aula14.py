'''for c in range (1,10):
    print(c)
print('Fim')'''
'''r=1
n='S'
while n == 'S':
    r=int(input('Digite um valor: '))
    n=str(input('Quer continuar? [s/n]: ')).upper()
print('Fim')'''
n=1
p=i=0
while n!=0:
    n=int(input('Digite um valor: '))
    if n!=0:
        if n%2==0:
            p+=1
        else:
            i+=1
print('Voce digitou {} par e {} impar.'.format(p,i))
print('Acabou!')