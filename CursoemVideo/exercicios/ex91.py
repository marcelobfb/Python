import random
import time
valores = {}
m = 0
for c in range(1, 5):
    valores[c] = random.randint(1, 6)
print('Valores Sorteados:')
for x, k in valores.items():
    print(f'O jogador de número {x} tirou {k} no dado.')
    time.sleep(0.5)
print('Ranking dos Jogadores:')
for s in sorted(valores, key=valores.get, reverse=True):#botar o dicionario em ordem
    m += 1
    print(f'{m} Lugar: Jogador de número {s} tirou {valores[s]}.')
    time.sleep(0.5)
