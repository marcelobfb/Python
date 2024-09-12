matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par=[]
for l in range(0,3):
    for c in range(0,3):
        n1=matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))
        if n1%2==0:
            par.append(n1)
print('-='*30)
print([matriz[0][0]], [matriz[0][1]], [matriz[0][2]])
print([matriz[1][0]], [matriz[1][1]], [matriz[1][2]])
print([matriz[2][0]], [matriz[2][1]], [matriz[2][2]])
print('-='*30)
print(f'A soma dos valores pares é {sum(par)}. ')
print(f'A soma dos valores da terceira coluna é {(matriz[0][2]+matriz[1][2]+matriz[2][2])}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
print('-='*30)