n1=int(input('Em que ano você nasceu? '))
n2=2023-n1
n3=n2-18
n4=18-n2
if n2==18:
    print('Você tem 18 anos está na hora de se alistar!')
elif n2>18:
    print('Você tem {} anos, ja passou {} anos do tempo do alistamento.'.format(n2,n3))
elif n2<18:
    print('Você tem {} anos, está quase na hora de se alistar, faltam {} anos.'.format(n1,n4))

