lista=[]
listapar=[]
listaimpar=[]
while True:
    n1=int(input('Digite um número: '))
    n2=str(input('Deseja continuar [S/N]? ')).strip().upper()
    lista.append(n1)
    if n1%2==0:
        listapar.append(n1)
    else:
        listaimpar.append(n1)
    if n2=='N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de par é {listapar}')
print(f'A lista de impar é {listaimpar}')