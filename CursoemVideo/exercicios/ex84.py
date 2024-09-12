lista = []
lista2 = []
qntp = 0
maior = 0
menor = 0
while True:
    n1 = lista.append(str(input('Nome: ')))
    n2 = lista.append(str(input('Peso: ')))
    n3 = str(input('Quer continuar [S/N]? ')).strip().upper()
    if len(lista2) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    lista2.append(lista[:])
    lista.clear()
    qntp += 1
    if n3 == 'N':
        break
print()
print(f'Ao todo, você cadastrou {qntp} pessoas.')
print()
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in lista2:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in lista2:
    if p[1] == menor:
        print(f'{p[0]}...', end='')
print()
