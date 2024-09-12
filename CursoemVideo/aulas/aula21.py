'''def contador(i, f, p):#comando help() usar 3 ".
    """
    -> Faz um contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


contador(0, 100, 10)
help(contador)'''
# -------------------------------------------
'''def soma(a=0,b=0,c=0):# se eu botar q a variavel recebe 0 eu to dizendo q se o cara n colocar nada vai ser 0.(parametro opcional)
    s=a+b+c
    print(f'a soma é {s}.')


soma(3,2,5)
soma(8,5)
soma()'''
# ------------------------------------
'''def teste():
    global n#se eu colocar isso aq eu vou estar usando 'n' global em ves do local
    n=3#essa variavel 'n' é diferente da variavel 'n' global pq ele é local, sao duas varaveis diferentes
    x=8#a varivael 'x' so tem escopo local entao se eu tentar printar ela la em baixo n vai dar certo
    print(f'na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')
n=2
teste()
print(f'no programa princiapl, n vale {n}.')#variavel 'n' tem um escopo global'''


# ------------------------------------------
'''def somar(a=0, b=0, c=0):#usar return
    s = a + b + c
    return s


n1 = somar(3, 4, 2)
n2 = somar(1, 2, 3)
n3 = somar(1, 1, 1)
print(f'Meus calculos deram {n1}, {n2} e {n3}')
'''
#------------------------------------
def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f


n=int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')