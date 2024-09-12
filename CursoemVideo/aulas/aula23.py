try:#vai tentar fazer
    n=int(input('num: '))
except:#se der erro vai mostrar isso, da pra botar tb except (e o nome do erro(s))
    print('Error')
else:#se n der erro vai mostrar isso
    print(f'vc digitou {n}')
finally:#vai mostrar isso dando erro ou nao
    print('Tente dnv')
