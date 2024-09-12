n1=str(input('Escreva uma frase: ')).strip()
print("A letra 'A' aparece {} vezes.".format(n1.upper().count('A')))
print("A letra 'A' aparece a primeira vez na posição {}.".format(n1.upper().find('A')+1))
print("A letra 'A' aparece pela última vez em {}.".format(n1.upper().rfind('A')+1))