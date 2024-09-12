# dicionarios
'''pessoas = {'nome': 'Marcelo', 'sexo': 'M', 'idade': '25'}'''
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())#mostra nome,sexo,idade
#print(pessoas.values())#mostra marcelo, m,25
#print(pessoas.items())#mostra tudo
#del pessoas['sexo']
#pessoas['nome']='Leandro'
#pessoas['peso']=98.5 #adiciona
'''for k,v in pessoas.items():
    print(f'{k}={v}')# Mostra nome=marcelo,sexo=m,idade=25,'''
#-------------------------------------------------------
'''brasil=[]
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''
#-------------------------------------------------------
'''estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())#cria uma copia do dicionario o [:] nao funciona em dicionario
for e in brasil:
    #for v in e.values():
        #print(v, end=' ')
    #print()
    for v,f in e.items():
        print(f'O {v} tem valor {f}.'''''
#for s in sorted(valores, key=valores.get, reverse=True):#botar o dicionario em ordem