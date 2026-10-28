x= int(input("Digite um número: "))
y = 1
for i in range(x,0,-1):
    if i >1:
        y = y * i
    else:
        break
print(f"O fatorial de {x} é: {y}")