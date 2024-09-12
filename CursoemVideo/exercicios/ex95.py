jogador = {}
gols = []
time = []
count = 0

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: ')).strip().capitalize()
    n1 = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(1, n1 + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-=' * 30)
    while True:
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
for k, v in enumerate(time):
    print(f'{k:>4} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-=' * 30)
