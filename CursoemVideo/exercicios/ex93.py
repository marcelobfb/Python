jogador={}
gols=[]
count=0
jogador['nome']=str(input('Nome: '))
n1=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1,n1+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
golssoma=sum(gols)
jogador['gols']=gols
jogador['total']=golssoma
print('-='*30)
print(jogador)
print('-='*30)
for x,p in jogador.items():
    print(f'O campo {x} tem o valor {p}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {n1} partidas.')
for g in jogador['gols']:
    count += 1
    print(f'Na partida {count}, fez {g} gols.')
print(f'Foi um total de {golssoma} gols.')