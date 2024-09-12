def leiaInt(b):
    global n
    while True:
        try:
            n = int(input(b))
        except (ValueError,TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m.')
            continue
        else:
            return n


def leiaFloat(b):
    global m
    while True:
        try:
            m = float(input(b))
        except (ValueError,TypeError):
            print('\033[31mERRO! Digite um número inteiro válido\033[m.')
            continue
        else:
            return m

try:
    n = leiaInt('Digite um número Inteiro: ')
    m = leiaFloat('Digite um número Real: ')
    print(f'Você acabou de digitar o número {n} e {m}.')
except KeyboardInterrupt:
    print('\n\n\033[31mObrigado por usar, tente novamente.\033[m')
