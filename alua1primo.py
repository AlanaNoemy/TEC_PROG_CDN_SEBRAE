while True:
    try:
     x = int(input('Digite um número: '))
     break
    except ValueError:
     print('Digite um número válido!')
def primo(x):
        if x >= 2 and x % 1 == 0 and x % x == 0:
            return f'O número {x} é primo.'
        else:
            return f'O número {x} não é primo.'
        
print(primo(x))