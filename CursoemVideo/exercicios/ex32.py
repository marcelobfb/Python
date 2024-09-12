n1=int(input('Qual é o ano? '))
if n1%4==0 and n1%100!=0 or n1%400==0:
    print('O ano de {} é bissexto.'.format(n1))
else:
    print('O ano não é bissexto.')