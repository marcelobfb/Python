lista=[]
while True:
    n2=int(input('Digite um número: '))
    if n2 not in lista:
        lista.append(n2)
        print(f'Valor {n2} adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    n1=str(input('Deseja continuar [S/N]: ')).strip().upper()
    if n1=='N':
        lista.sort()
        print(f'Você digitou os valores {lista}.')
        break
