print('-' * 30)
print('LOJA DO CELOV')
print('-' * 30)
lista2 = []
p1k = menor = cont = maior = 0
barato = caro = ''
while True:
    n1 = str(input('Nome do produto: ')).strip().upper()
    n2 = float(input('Preço: R$'))
    cont += 1
    lista2 += [n2]
    print('-' * 30)
    n3 = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('-' * 30)
    if n2 > 1000:
        p1k += 1
    if cont == 1:
        menor = n2
        barato = n1
        maior = n2
        caro = n1
    else:
        if n2 < menor:
            menor = n2
            barato = n1
        if n2 > maior:
            maior = n2
            caro = n1
    if n3 == 'N':
        print(f'Temos {p1k} produtos que custaram mais de R$1.000,00.')
        print(f'O total das compras foi R${sum(lista2)}.')
        print(f'O produto mais barato é {barato} e custa R${menor}')
        print(f'O produto mais caro é {caro} e custa R${maior}')
        break
