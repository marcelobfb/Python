lista = []
while True:
    n1 = lista.append(int(input('Digite um número: ')))
    n2 = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if n2 == 'N':
        print(f'Você digitou {len(lista)} elementos.')
        lista.sort(reverse=True)
        print(f'Os valores em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da sua lista.')
        else:
            print('O valor 5 não faz parte da sua lista.')
        break
