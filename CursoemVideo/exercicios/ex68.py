import random
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
r1=0
c1=0
while True:
    n1=int(input('Digite um valor: '))
    n2=str(input('Par ou Ímpar [P/I]? ')).strip().upper()
    r1 = random.randint(1, 10)
    if n2=='P':
        if (n1+r1)%2==0:
            print('=-' * 15)
            print(f'Você jogou {n1} e o computador jogou {r1}. Total de {n1+r1} deu PAR.')
            print('Você \033[32mganhou\033[m.')
            c1 += 1
            print('=-' * 15)
        if (n1+r1)%2!=0:
            print('=-' * 15)
            print(f'Você jogou {n1} e o computador jogou {r1}. Total de {n1+r1} deu IMPAR.')
            print('Você \033[31mperdeu\033[m, você ganhou um total de {}x.'.format(c1))
            print('=-' * 15)
            break
    if n2=='I':
        if (n1+r1)%2!=0:
            print('=-' * 15)
            print(f'Você jogou {n1} e o computador jogou {r1}. Total de {n1+r1} deu IMPAR.')
            print('Você \033[32mganhou\033[m.')
            c1+=1
            print('=-' * 15)
        if (n1+r1)%2==0:
            print('=-' * 15)
            print(f'Você jogou {n1} e o computador jogou {r1}. Total de {n1+r1} deu PAR.')
            print('Você \033[31mperdeu\033[m, você ganhou um total de {}x.'.format(c1))
            print('=-' * 15)
            break

