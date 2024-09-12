print('{:=^40}'.format('\033[;31mLojas BFB\033[m'))

n1=float(input('Qual o preço do produto? R$'))
n2=int(input('''Qual o seu metodo de pagamento?
[1] À VISTA dinheiro/cheque: 10% de desconto.
[2] À VISTA no cartão 05% de desconto.
[3] Em até 02x no cartão: Preço normal.
[4] 3x ou mais no cartão: 20% de juros.
Opção: '''))
if n2==1:
    print('À vista dinheiro/cheque: 10% de desconto, o valor total é de: R${}.'.format(n1-(n1*0.1)))
elif n2==2:
    print('À vista no cartão 05% de desconto, o valor total é de R${}.'.format(n1-(n1*0.05)))
elif n2==3:
    print('Em até 02x no cartão, o valor total é de R${}.'.format(n1))
elif n2==4:
    n3=int(input('Quantas parcelas? '))
    n4= n1*0.2
    n5= n4+n1
    print('Sua compra sera parcelada em {}x de R${} com 20% de juros mensal.'.format(n3, (n5/n3)))
    print('O valor total é de R${}.'.format(n1+n4))
else:
    print('Número invalido, tente novamente.')