def soma(a, b):
    return f" {a} + {b} : {a + b}"

while True:
    try:
     a = float(input('Digite um número: '))
     b = float(input('Digite um número: '))    
     break      
    except ValueError:
                    print('Digite um número válido!')
print(soma(a, b))