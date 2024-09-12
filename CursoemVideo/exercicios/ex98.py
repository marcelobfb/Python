def contador(a, b, c):
    if c < 0:
        print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if c > 0:
        print(f'Contagem de {a} até {b} de {c} em {c}.')
    if c == 0:
        print(f'Contagem de {a} até {b} de 1 em 1.')
    if a < b and c != 0 and c > 0:
        for c in range(a, b + 1, c):
            print(c, end=' ')
        print('FIM!')
    elif a > b and c != 0 and c > 0:
        for c in range(a, b - 1, -c):
            print(c, end=' ')
        print('FIM!')
    elif c < 0:
        for c in range(a, b - 1, c):
            print(c, end=' ')
        print('FIM!')
    elif c == 0 and a < b:
        for c in range(a, b + 1, c + 1):
            print(c, end=' ')
        print('FIM!')
    elif c == 0 and a > b:
        for c in range(a, b - 1, -(c + 1)):
            print(c, end=' ')
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
m = int(input('Início: '))
k = int(input('Fim: '))
p = int(input('Passo: '))
contador(m, k, p)
