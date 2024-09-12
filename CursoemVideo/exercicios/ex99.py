from time import sleep
def maior(*num):
    ordenado=tuple(sorted(num, reverse=True))
    le=len(num)
    print('-'*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}',end=' ')
        sleep(0.3)
    print(f'foram informados {le} valores ao todo.')
    print(f'O maior número é {ordenado[0]}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
print()
