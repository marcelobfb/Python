import random
from time import sleep
n1=str(input('Eu contra tu, pedra, papel e tesouuuraaa: ')).upper()
print('-='*15)
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO')
n2={'Pedra','Papel','Tesoura'}
n3=(random.choice(list(n2)))
print('-='*15)
print('Você jogou \033[35m{}\033[m.'.format(n1.capitalize()))
print('O computador jogou \033[33m{}\033[m.'.format(n3))
print('-='*15)
if n1=='PEDRA'and n3=='Pedra':
    print('Você \033[37mempatou\033[m!')
elif n1=='PEDRA'and n3=='Tesoura':
    print('Parabéns você \033[34mganhou\033[m!')
elif n1=='PEDRA'and n3=='Papel':
    print('Você \033[31mperdeu\033[m!')
elif n1 == 'TESOURA' and n3 == 'Tesoura':
    print('Você \033[37mempatou\033[m!')
elif n1 == 'TESOURA' and n3 == 'Papel':
    print('Parabéns você \033[34mganhou\033[m!')
elif n1 == 'TESOURA' and n3 == 'Pedra':
    print('Você \033[31mperdeu\033[m!')
elif n1 == 'PAPEL' and n3 == 'Papel':
    print('Você \033[37mempatou\033[m!')
elif n1 == 'PAPEL' and n3 == 'Pedra':
    print('Parabéns você \033[34mganhou\033[m!')
elif n1 == 'PAPEL' and n3 == 'Tesoura':
    print('Você \033[31mperdeu\033[m!')
print('-='*15)