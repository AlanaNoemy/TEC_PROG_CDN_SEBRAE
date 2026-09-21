'''
#testes anteriores (green)
class Calculadora:
    def somar(self, a, b):
        return a + b
   
    def dividir(self, a, b):
        if b ==0:
            raise ValueError("Não é possivel dividir por zero.!")
        return a / b
'''
class Calculadora:
    def __init__(self):
        self._ultimo_resultado = None

    def somar(self, a, b):
        self._ultimo_resultado = a + b
        return self._ultimo_resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        self._ultimo_resultado = a / b
        return self._ultimo_resultado

    @property
    def ultimo_resultado(self):
        return self._ultimo_resultado