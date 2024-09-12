import datetime
pessoas = {}
pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
pessoas['idade'] = int(input('Ano de nascimento: '))
pessoas['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoas['ctps']==0:
    pessoas['idade'] = datetime.datetime.now().year - pessoas['idade']
    print('-=' * 40)
    for x,y in pessoas.items():
        print(f'{x} tem o valor {y}.')
if pessoas['ctps'] != 0:
    pessoas['anocontra'] = int(input('Ano de contratação: '))
    pessoas['salario'] = float(input('Salário: '))
    print('-=' * 40)
    print(pessoas)
    pessoas['aposentadoria'] = (pessoas['anocontra'] - pessoas['idade']) + 35
    pessoas['idade'] = datetime.datetime.now().year - pessoas['idade']
    for x, y in pessoas.items():
        print(f'{x} tem o valor {y}.')

