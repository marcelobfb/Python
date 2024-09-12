def fatorial(num=1, show=False):
    """
    calcula o fatorial de um numero
    :param num: o numero a ser calculado
    :param show: mostra  ou nao a conta
    :return: o valor do fatorial de um numero n
    """
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            f *= c
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        return f
    else:
        for c in range(num, 0, -1):
            f *= c
        return f


print(fatorial(5))
help(fatorial)
