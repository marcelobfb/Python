def leiaInt(b):
    global n
    while True:
        n = str(input(b))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m.')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
