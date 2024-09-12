import random
n1=(random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10))
print(f'Os valores sorteados foram {n1}.')
print('O maior valor sorteado foi {}'.format(sorted(n1)[-1]))
print(f'O menor valor sorteado foi {sorted(n1)[0]}')