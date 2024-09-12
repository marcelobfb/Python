tabela=('botafogo','palmeiras','gremio','flamengo','fluminense','bragantino','athelico-pr','fortaleza','atletico-mg',
        'cuiaba','sp','cruzeiro','corinthians','inter','goias','bahia','santos','vasco','coritiba','america-mg')
print('Os 5 primeiros colocados são {}.'.format(tabela[0:5]))
print(f'Os 4 ultimos são {tabela[-4:]}')
print(f'Os times em ordem alfabetica é {sorted(tabela)}')
print('O flamengo esta na posição {}.'.format(tabela.index('flamengo')+1))