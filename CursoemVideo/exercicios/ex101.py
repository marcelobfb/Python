import time
def voto(ani):
    global ano
    global n1
    i=ano-n1
    if 18 <= i < 65:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    elif i<18:
        return 'Com {i} anos: NÃO VOTA.'
    elif i>=65:
        return 'Com {i} anos: VOTO OPCIONAL.'


ano=time.localtime().tm_year
n1=int(input('Em que ano você nasceu? '))
print(voto(n1))