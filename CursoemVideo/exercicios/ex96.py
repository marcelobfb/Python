def area(a, b):
    c = a * b
    print(f'A área de um terreno de {a}x{b} é de {c}m2. ')


print('Controle de Terrenos')
print('-' * 20)
la = float(input('Largura (m): '))
co = float(input('Comprimento (m): '))
area(la, co)
