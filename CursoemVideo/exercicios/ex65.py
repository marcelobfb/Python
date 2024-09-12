n1=0
n2=' '
list=[]
cont=0
while n2 != 'N':
    n1 = int(input('Digite um número: '))
    n2 = str(input('Quer continuar [S/N]: ')).upper()
    list+=[n1]
    cont+=1
n5=sum(list)
n6=len(list)
media=n5/n6
list.sort()
print('Você digitou {} números e média entre eles foi {}.'.format(cont,media))
print('O menor número foi {} e o maior foi {}.'.format(list[0],list[-1]))