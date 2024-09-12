lista = [[], [], []]
count = 0
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    print('-='*30)
    n = str(input('Deseja continuar [S/N]? ')).strip().upper()
    print('-='*30)
    lista[0].append(nome)
    lista[1].append(nota1)
    lista[2].append(nota2)
    count += 1
    if n == 'N':
        break
print(lista)
print('-=' * 50)
for c in range(0, count):
    print(f'''Matricula: {c}.
Nome: {lista[0][c]}.
Média: {(lista[1][c] + lista[2][c]) / 2:.2f}.''')
    print('-='*30)
while True:
    continua = int(input('Deseja mostrar nota de qual matricula (999 interrompe)? '))
    print('-='*30)
    if continua!=999:
        print(f'Notas de {lista[0][continua]} são {lista[1][continua]:.2f} e {lista[2][continua]:.2f}.')
        print('-='*30)
    if continua == 999:
        print('Obrigado, volte sempre!')
        break
