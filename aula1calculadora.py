#aula tecnicas da programação em python

# funçãos do menu de opções

def soma(a, b):
    return f" {a} + {b} : {a + b}"
def subtracao(a, b):
    return f" {a} - {b} : {a - b}"
def multiplicacao(a, b):
    return f" {a} x {b} : {a * b}"
def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return f" {a} / {b} : {a / b}"
# main (corpo do codigo)
while True:
     print(" ==== MENU DE OPÇÕES ====")
     print(" 1 - Somar dois números \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair")
     while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            break
        except ValueError:
            print("Digite uma opção válida!")
     if opcao in [1, 2, 3, 4]:
       while True:
        try:
            a = float(input('Digite um número: '))
            b = float(input('Digite um número: '))    
            break      
        except ValueError:
                    print('Digite um número válido!')
                    
     if opcao == 1:
       print(soma(a, b))
     elif opcao == 2:
         print(subtracao(a, b))
     elif opcao == 3:
         print(multiplicacao(a, b))
     elif opcao == 4:
         print(divisao(a, b))
     elif opcao == 5:
         print("Saindo do programa...")
         break
     else:
         print("Opção inválida!")
    