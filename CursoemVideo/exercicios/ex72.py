n=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze',
   'quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    n1=int(input('Digite um número entre 0 e 20: '))
    if n1>=0 and n1<=20:
        print(f'Você digitou o número {n[n1]}.')
        break


