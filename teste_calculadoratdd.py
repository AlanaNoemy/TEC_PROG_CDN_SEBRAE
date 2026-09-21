import unittest
from calculadoratdd import Calculadora


class TestCalculadora(unittest.TestCase):
    def test_somar_dois_numeros_positivos(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(2, 3), 5)

    def test_dividir_dois_numeros(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)

    def test_deve_armazenar_ultimo_resultado(self):
        calc = Calculadora()
        calc.somar(10, 5)
        self.assertEqual(calc.ultimo_resultado, 15)

    def test_deve_lancar_erro_ao_dividir_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)


if __name__ == '__main__':
    unittest.main()
