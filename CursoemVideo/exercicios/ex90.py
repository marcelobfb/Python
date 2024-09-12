aluno={}
aluno['Nome']=str(input('Nome: ')).capitalize().strip()
aluno['Média']=float(input('Média: '))
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
if aluno['Média']>=6:
    print('A situação é igual a Aprovado.')
else:
    print('A situação é igual a Reprovado.')