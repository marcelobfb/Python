n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
n3 = int(input('Digite um terceiro valor: '))
n4 = int(input('Digite um quarto valor: '))
n5 = (n1,n2,n3,n4)
#print(n5)
print(f'O valor 9 apareceu {n5.count(9)}x.')
if n5.count(3)>0:
    print(f'O valor 3 apareceu na {n5.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
for n in n5:
    if n%2==0:
        print(f'O número {n} é par.')
