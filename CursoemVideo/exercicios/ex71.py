print('-='*15)
print('{:^30}'.format('BANCO CELOV'))
print('-='*15)
valor=int(input('Que valor você quer sacar? R$'))
total=valor
ced=50
totdced=0
while True:
    if total>=ced:
        total-=ced
        totdced+=1
    else:
        if totdced>0:
            print(f'Total de {totdced} cedulas de R${ced}.')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totdced=0
        if total==0:
            break