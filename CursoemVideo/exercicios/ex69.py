print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
n18=0
h=0
m=0
while True:
    n1=int(input('Idade: '))
    n2=str(input('Sexo [M/F]: ')).strip().upper()
    if n1>18:
        n18+=1
    if n2=='M':
        h+=1
    if n2=='F'and n1<20:
        m+=1
    n3=str(input('Deseja continuar [S/N]? ')).strip().upper()
    if n3=='N':
        print('-' * 20)
        print('Obrigado!')
        print('-' * 20)
        print(f'Quantas pessoas tem mais de 18 anos? {n18}.')
        print(f'Quantos homens foram cadastrados? {h}.')
        print(f'Quantas mulheres menos de 20 anos? {m}')
        break
    if n3=='S':
        print('-' * 20)
