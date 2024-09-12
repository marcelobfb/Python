galera = []
ridade = []
pessoas = {}
mulheres = []
mulheres2=[]
countp = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Porfavor, digite apenas M ou F.')
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    ridade.append(pessoas['idade'])
    galera.append(pessoas.copy())
    while True:
        n1 = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if n1 in 'SN':
            break
        print('ERRO! Porfavor, digite apenas S ou N.')
    countp += 1
    if n1 == 'N':
        break
media=((sum(ridade)) / countp)
print(f'O grupo tem {countp} pessoas.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram {mulheres}.')
print(f'Lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade']>=media:
        print()
        for k,v in p.items():
            print(f'{k}={v}')
print()
print(galera)
