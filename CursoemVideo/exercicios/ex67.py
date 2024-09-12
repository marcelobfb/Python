while True:
    n1=int(input('Quer ver a tabuada de qual valor? '))
    if n1<0:
        print('Programa encerrado.')
        break
    if n1>0:
        for c in range(1,11):
            print(f'{n1} x {c} = {n1*c}')
