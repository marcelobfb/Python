from random import randint
números=[]
par=[]
def sorteia():
    for n in range(1,6):
        l=números.append(randint(1,10))
    print(f'Sorteando 5 valores da lista:',end=' ')
    for c in números:
        print(c,end=' ')
    print('PRONTO!')
sorteia()
def somaPar():
    for c in números:
        if c%2==0:
            par.append(c)
    x=sum(par)
    print(f'Somando os valores pares de {números}, temos {x}')
somaPar()
