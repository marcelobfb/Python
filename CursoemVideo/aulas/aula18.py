'''teste=[]
teste.append('Gustavo')
teste.append(40)
galera=[]
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)'''
#-------------------
'''galera=[['Joao',19],['Ana',33]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
#--------------------
'''galera=[]
dado=[]
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')'''