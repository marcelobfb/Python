from datetime import date
ano=date.today().year
n0=0
con=0
con2=0
for c in range(1,8):
    n0+=1
    n1 = int(input('Em que ano nasceu a {} pessoa? '.format(n0)))
    if (ano-n1)<18:
        con+=1
    if (ano-n1)>=18:
        con2+=1
print('{} pessoas já atingiram a maioridade e {} não.'.format(con2,con))