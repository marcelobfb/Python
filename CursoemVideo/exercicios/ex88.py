import random
import time
lista = []
jogos=[]
n1 = int(input('Quantos jogos você quer que eu sorteie? '))
tot=1
while tot<=n1:
    count = 0
    while True:
        num=random.randint(1,60)
        if num not in lista:
            lista.append(num)
            count+=1
        if count>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3,f'SORTEANDO {n1} JOGOS','-='*3)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(0.5)
