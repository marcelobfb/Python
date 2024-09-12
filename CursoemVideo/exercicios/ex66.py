n2=0
s=0
while True:
    n1=int(input('Digite um numero: '))
    if n1==999:
        break
    n2+=1
    s+=n1
print(f'A soma dos {n2} valores foi {s}!')