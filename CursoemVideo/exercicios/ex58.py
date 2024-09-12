import random

print('Que número estou pensando de 1 a 10. ')
n1 = random.randint(1, 10)
acertou = False
n3 = 0
while not acertou:
    n2 = int(input('Qual o número? '))
    n3 += 1
    if n1 == n2:
        acertou = True
    else:
        if n2 < n1:
            print('Muito baixo!')
        if n2 > n1:
            print('Muito alto!')
print('Voce acertou, levou exatas {} tentativas.'.format(n3))
