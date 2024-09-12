n1 = str(input('Qual seu sexo [M/F]: ')).upper().strip()
while n1 != 'F' and n1 != 'M':
    n1 = str(input('Dados invalidos, Qual seu sexo [M/F]: ')).upper().strip()
    if n1=='M':
        print('Sexo masculino registrado com sucesso.')
    if n1=='F':
        print('Sexo feminino registrado com sucesso.')
