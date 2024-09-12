s = 0
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n=n+1
        print(c)
        s += c
print('A soma de todos os números impares entre 1 e 500 é {}'.format(s))
print('Foram solicitados {} valores.'.format(n))
