'''fonte = {'nd': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul': '\033[34m', 'roxo': '\033[35m', 'branco': '\033[97m'}
fundo = {'nd': '\033[m', 'vermelho': '\033[0;30;41m', 'verde': '\033[0;30;42m', 'amarelo': '\033[0;30;43m',
         'azul': '\033[0;30;44m', 'roxo': '\033[0;30;45m', 'branco': '\033[7;30m'}
print(f'{fonte["vermelho"]}Clube{fonte["nd"]}{fonte["amarelo"]} de {fonte["nd"]}{fonte["azul"]}Regatas{fonte["nd"]}')
'''
# Dicionário de cores
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'verde': '\033[32m',
    'vermelho': '\033[31m',
}

while True:
    comando = input(f'Digite o comando (ou "FIM" para sair): {cores["azul"]}')

    if comando.upper() == 'FIM':
        print(f'{cores["vermelho"]}Saindo do sistema...{cores["limpa"]}')
        break

    print(f'{cores["verde"]}Ajuda para o comando "{comando}":{cores["limpa"]}')
    help(comando)
