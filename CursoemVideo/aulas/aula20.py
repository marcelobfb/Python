'''def linha():#função sem parametro
    print('-'*30)


linha()
print('Alo mundo')
linha()'''
# ----------------------------
'''def mensagem(msg):#função com parametro
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('alou')'''
# -----------------------------
'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)


# ou
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=3, a=2)'''
# -----------------------------
def contador(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}.')


contador(2,1,7)


# ------------------------------
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 2, 3, 5, 4, 2]
dobra(valores)
print(valores)'''
