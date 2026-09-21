l = []
for i in range(1, 101):
    if i >= 2 and i % 1 == 0 and i % i == 0:
        l.append(i)
        
print(f'Os números primos de 1 a 100 são: {l}')