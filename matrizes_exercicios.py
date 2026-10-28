def matrix_transpose(matrix):
    if not matrix or not matrix[0]:
        return []
    return [list(linha) for linha in zip(*matrix)]


def matrix_opposite(matrix):
    return [[-valor for valor in linha] for linha in matrix]


def matrix_add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("As matrizes precisam ter as mesmas dimensões.")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_subtract(a, b):
    return matrix_add(a, matrix_opposite(b))


def matrix_multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B.")
    result = []
    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            linha.append(total)
        result.append(linha)
    return result


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    total = 0
    for j in range(n):
        menor = [linha[:j] + linha[j + 1:] for linha in matrix[1:]]
        sinal = 1 if j % 2 == 0 else -1
        total += sinal * matrix[0][j] * determinant(menor)
    return total


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return None
    if len(matrix) == 2 and len(matrix[0]) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return [[d / det, -b / det], [-c / det, a / det]]

    cofatores = []
    for i in range(len(matrix)):
        linha = []
        for j in range(len(matrix[0])):
            menor = [linha_menor for idx, linha_menor in enumerate(matrix) if idx != i]
            menor = [coluna[:j] + coluna[j + 1:] for coluna in menor]
            sinal = 1 if (i + j) % 2 == 0 else -1
            linha.append(sinal * determinant(menor))
        cofatores.append(linha)
    adjunta = matrix_transpose(cofatores)
    return [[valor / det for valor in linha] for linha in adjunta]


def classify_matrix(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0]) if linhas else 0
    ordem = f"{linhas}x{colunas}"

    if linhas == 0:
        return f"matriz vazia, ordem {ordem}"
    if linhas == 1 and colunas == 1:
        return f"matriz 1x1, ordem {ordem}"
    if linhas == 1:
        return f"matriz linha, ordem {ordem}"
    if colunas == 1:
        return f"matriz coluna, ordem {ordem}"
    if linhas == colunas:
        if all(matrix[i][j] == 0 for i in range(linhas) for j in range(colunas) if i != j):
            if all(matrix[i][i] == 1 for i in range(linhas)):
                return f"matriz identidade, ordem {ordem}"
            if all(matrix[i][i] == 0 for i in range(linhas)):
                return f"matriz diagonal nula, ordem {ordem}"
            return f"matriz diagonal, ordem {ordem}"
        if all(matrix[i][j] == 0 for i in range(linhas) for j in range(colunas) if i > j):
            return f"matriz triangular superior, ordem {ordem}"
        if all(matrix[i][j] == 0 for i in range(linhas) for j in range(colunas) if i < j):
            return f"matriz triangular inferior, ordem {ordem}"
        return f"matriz quadrada, ordem {ordem}"
    return f"matriz retangular, ordem {ordem}"


def format_matrix(matrix):
    if not matrix:
        return "[]"
    return "\n".join("  ".join(str(x) for x in linha) for linha in matrix)


def resolver_exercicio_8():
    print("Exercício 8: determinantes")
    matrizes = {
        "a) A": [[2, 4], [3, 8]],
        "b) B": [[-1, -5], [6, 2]],
        "c) C": [[-7, 5], [-8, -3]],
        "d) W": [[1, 2, 3], [0, 1, 2], [-1, 2, 0]],
        "e) X": [[0, 1, 1], [2, 3, 1], [-1, 0, 4]],
    }
    for nome, matriz in matrizes.items():
        print(f"{nome} = det({nome}) = {determinant(matriz)}")
    print()


def resolver_exercicio_9():
    print("Exercício 9: existência da inversa")
    matrizes = {
        "a": [[2, 1], [-1, 3]],
        "b": [[3, -1], [-6, 2]],
        "c": [[2, 0, -1], [4, 1, 3], [6, 2, 7]],
        "d": [[2, -1, 3], [0, 1, 2], [-3, 4, 1]],
    }
    for nome, matriz in matrizes.items():
        det = determinant(matriz)
        print(f"{nome}: det = {det}; inversa existe? {'sim' if det != 0 else 'não'}")
        if det != 0:
            print(f"Inversa de {nome}:\n{format_matrix(inverse(matriz))}\n")
    print()


def resolver_exercicio_1():
    print("Exercício 1")
    a = [[1, 2], [-1, -4]]
    print("A =", format_matrix(a))
    print("a) Transposta de A:", format_matrix(matrix_transpose(a)))
    print("b) Oposta de A:", format_matrix(matrix_opposite(a)))
    print()


def resolver_exercicio_2():
    print("Exercício 2")
    matrizes = {
        "a) A": [[1, 3], [0, 1]],
        "b) B": [[1, 4, 5]],
        "c) C": [[1], [2], [-1]],
        "d) D": [[1, 0, 0], [0, 3, 0], [0, 0, 4]],
        "e) E": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    }
    for letra, (nome, matriz) in enumerate(matrizes.items(), start=1):
        print(f"{chr(96 + letra)}) {nome}: {classify_matrix(matriz)}")
    print()


def resolver_exercicio_3():
    print("Exercício 3")
    a = [[1, 2], ["a", 3]]
    b = [["x", 3], ["b", 3]]
    print("A =", format_matrix(a))
    print("B =", format_matrix(b))
    print("Como A = B^T, então B^T = [[x, b], [3, 3]].")
    print("Comparando com A = [[1, 2], [a, 3]], temos:")
    print("x = 1, b = 2 e a = 3.")
    print()


def resolver_exercicio_4():
    print("Exercício 4")
    a = [[2, 3], [1, 4]]
    b = [[3, -1], [-2, 4]]
    print("a) A + B =", format_matrix(matrix_add(a, b)))
    print("b) 2B + A =", format_matrix(matrix_add([[2 * valor for valor in linha] for linha in b], a)))
    print("c) A - 3B =", format_matrix(matrix_subtract(a, [[3 * valor for valor in linha] for linha in b])))
    print("d) A^T + B^T =", format_matrix(matrix_add(matrix_transpose(a), matrix_transpose(b))))
    print("e) (A + B)^T =", format_matrix(matrix_transpose(matrix_add(a, b))))
    print()


def resolver_exercicio_5():
    print("Exercício 5")
    a = [[2, 3, 1], [0, 0, -2]]
    b = [[1, 0], [0,4], [-1, 2]]
    c = [[2], [1]]
    ab = matrix_multiply(a, b)
    print("a) A · B =", format_matrix(ab))
    print("b) (A · B) · C =", format_matrix(matrix_multiply(ab, c)))
    print()


def resolver_exercicio_6():
    print("Exercício 6")
    a = [[2, 1], [0, 5]]
    b = [[5, 3], [2, 0]]
    print("a) (A · B)^T =", format_matrix(matrix_transpose(matrix_multiply(a, b))))
    print("b) A^T · B^T =", format_matrix(matrix_multiply(matrix_transpose(a), matrix_transpose(b))))
    print()


def resolver_exercicio_7():
    print("Exercício 7")
    a = [[2, 3], [4, -1], [0, 1]]
    a2 = [[2, 4, 1], [-1, 3, 0]]
    b = [[0, -1], [2, 3], [-1, 1]]
    b2 = [[0, 1], [-1, -1]]
    c = [[2,4],[-1,1]]
    c2 = [[3,1], [2,2], [4 ,0]]
    d = [[2],[4],[-1]]
    d2 = [[2,3,-1]]
    print("a) ", format_matrix(matrix_multiply(a, a2)))
    print("b) ", format_matrix(matrix_multiply(b, b2)))
    print("c) não é possível multiplicar c e c2, pois o número de colunas de c (2) não é igual ao número de linhas de c2 (3).")
    print("d) não é possível multiplicar d e d2, pois o número de colunas de d (1) não é igual ao número de linhas de d2 (3).")


def main():

    resolver_exercicio_1()
    resolver_exercicio_2()
    resolver_exercicio_3()
    resolver_exercicio_4()
    resolver_exercicio_5()
    resolver_exercicio_6()
    resolver_exercicio_7()
    resolver_exercicio_8()
    resolver_exercicio_9()


if __name__ == "__main__":
    main()
