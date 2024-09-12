s = 0
n = 0
for c in range(1, 7):
    n1 = int(input('Digite o {} numero: '.format(c)))
    if n1 % 2 == 0:
        n += n1
        s += 1
print('Voce informou {} numeros pares e a soma foi {}.'.format(s, n))
