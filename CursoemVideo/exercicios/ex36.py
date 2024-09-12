print('Boa tarde!')
casa = float(input('Qual o valor da casa? R$'))
renda = float(input('Qual sua renda mensal? R$'))
ano = int(input('Quantos anos você pretende pagar? '))
#calcule o valor da prestação mensal. sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo será negado.
max = renda*0.30
meses = ano*12
parcelas = casa/meses
if parcelas<=max:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de R${:.2f}, emprestimo pode ser concedido.'.format(casa,ano,parcelas))
elif parcelas>max:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de R${:.2f}, seu emprestimo não foi aprovado, por ter passado seu limite mensal de R${:.2f}.'.format(casa,ano,parcelas,max))
