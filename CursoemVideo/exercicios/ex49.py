n1 = int(input('''Qual tabuada você deseja?
 [ 1 ] +
 [ 2 ] -
 [ 3 ] *
 [ 4 ] / 
Digite o codigo: '''))
if n1 == 3:
    n2 = int(input('Digte um número para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} x {:2} = {:2}.'.format(n2, c, n2 * c))
elif n1 == 1:
    n3 = int(input('Digte um número para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} + {:2} = {:2}.'.format(n3, c, n3 + c))
elif n1 == 2:
    n4 = int(input('Digte um número para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} - {:2} = {:2}.'.format(n4, c, n4 - c))
elif n1 == 4:
    n5 = int(input('Digte um número para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} / {:2} = {:2}.'.format(n5, c, n5 / c))
else:
    print('Tente novamente.')
