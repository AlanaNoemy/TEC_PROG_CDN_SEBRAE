a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "Não existem raízes reais."
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        return f"As raízes são: x1 = {x1} e x2 = {x2}"

print(bhaskara(a, b, c))