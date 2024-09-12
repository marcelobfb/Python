import datetime
n1=int(input('Em que ano você nasceu? '))
n2=2023-n1
if n2<=9:
    print('Você tem {} anos, sendo um atleta MIRIM.'.format(n2))
elif n2>9 and n2<=14:
    print('Voce tem {} anos, sendo um atleta INFANTIL.'.format(n2))
elif n2>14 and n2<=19:
    print('Voce tem {} anos, sendo um atleta JUNIOR.'.format(n2))
elif n2>=20:
    print('Voce tem {} anos, sendo um atle MASTER.'.format(n2))