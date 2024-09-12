def metade(n, x=False):
    res = n / 2
    if x == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res


def dobro(n, x=False):
    res = n * 2
    if x == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res


def aumentar(a, b, c=False):  # aumentar porcetangem
    x = a * (b / 100)
    res = a + x
    if c == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res


def diminuir(c, d, f=False):  # diminuir porcentagem
    x = c * (d / 100)
    res = c - x
    if f == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(p, a, r):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'80% de aumento: \t{aumentar(p, a, True)}')
    print(f'35% de redução: \t{diminuir(p, r, True)}')
    print('-' * 30)
