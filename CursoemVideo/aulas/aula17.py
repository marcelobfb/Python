#listas
#lanche=['hamburguer','suco','pizza','pudim']
#lanche.append('cookie')#adicionar um elemento no final
#lanche.insert(0,'Cachorro')#adicionar em qualquer outra posição
#del lanche[3]#elimina um elemento
#lanche.pop(3)#elimina um elemento q vc escolhe ou o ultimo elemento se n tiver nd
#lanche.remove('pizza')#remove pelo conteudo e n pela posição
#if 'pizza' in lanche: #se tiver a pizza no lanche ele remove
   # lanche.remove('pizza')
#print (lanche)
#-------------------
#valores=list(range(4,11)) #cria uma lista em um range
#valores.sort() #vai ordernar os valores
#valores.sort(reverse=True) #ordernar ao inverso
#len(valores) #vai dizer quantos elementos tem na tabela
#----------------------------
'''valor=[]
for cont in range (0,5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'na posição {c} encontrei o valor {v}!')
print (valor)'''
a=[2,3,4,5]
#b=a #elas estão ligadas
b=a[:]#cria uma copia dos valores de 'a'
b[2]=8
print(f'Lista A: {a}')
print(f'Lista B: {b}')