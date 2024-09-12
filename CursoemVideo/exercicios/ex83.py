pilha=[]
expr=str(input('Digite a expressão: '))
for simb in expr:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressao esta valida.')
else:
    print('Sua expressao esta errada.')