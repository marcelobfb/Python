lista = [[], []]
for c in range(1, 8):
    n1 = int(input(f'Digite o {c} número: '))
    if n1 % 2 == 0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)
lista.sort()
print('-='*30)
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números impares digitados foram: {lista[1]}')