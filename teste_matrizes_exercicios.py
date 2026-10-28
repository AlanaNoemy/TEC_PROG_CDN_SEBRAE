import unittest

from matrizes_exercicios import (
    determinant,
    inverse,
    matrix_add,
    matrix_multiply,
    matrix_opposite,
    matrix_transpose,
)


class TestMatrizesExercicios(unittest.TestCase):
    def test_transposta(self):
        a = [[1, 2], [-1, -4]]
        self.assertEqual(matrix_transpose(a), [[1, -1], [2, -4]])

    def test_oposta(self):
        a = [[1, 2], [-1, -4]]
        self.assertEqual(matrix_opposite(a), [[-1, -2], [1, 4]])

    def test_determinante_2x2(self):
        a = [[2, 4], [3, 8]]
        self.assertEqual(determinant(a), 4)

    def test_determinante_3x3(self):
        a = [[1, 2, 3], [0, 1, 2], [-1, 2, 0]]
        self.assertEqual(determinant(a), -5)

    def test_soma_de_matrizes(self):
        a = [[2, 3], [1, 4]]
        b = [[3, -1], [-2, 4]]
        self.assertEqual(matrix_add(a, b), [[5, 2], [-1, 8]])

    def test_multiplicacao_de_matrizes(self):
        a = [[2, 3], [1, 4]]
        b = [[5, 3], [2, 0]]
        self.assertEqual(matrix_multiply(a, b), [[16, 6], [13, 3]])

    def test_inversa_2x2(self):
        a = [[2, 1], [-1, 3]]
        self.assertEqual(inverse(a), [[0.42857142857142855, -0.14285714285714285], [0.14285714285714285, 0.2857142857142857]])


if __name__ == '__main__':
    unittest.main()
