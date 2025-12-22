import numpy as np


def solve_system_cholesky(A, b):
    """
    Решение системы линейных уравнений методом Холецкого

    Параметры:
    A - матрица коэффициентов (numpy.matrix или numpy.ndarray)
    b - вектор свободных членов (numpy.array)

    Возвращает:
    L - нижняя треугольная матрица
    U - верхняя треугольная матрица
    x - решение системы
    y - промежуточный вектор
    residual - вектор невязки
    """

    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.eye(n)

    # LU-разложение
    for i in range(n):
        # Вычисляем столбец i матрицы L
        for j in range(i, n):
            L[j, i] = A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))

        # Вычисляем строку i матрицы U
        for j in range(i + 1, n):
            U[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))) / L[i, i]

    # Прямая подстановка: Ly = b
    y = np.zeros(n)
    for i in range(n):
        s = sum(L[i, k] * y[k] for k in range(i))
        y[i] = (b[i] - s) / L[i, i]

    # Обратная подстановка: Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = sum(U[i, j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - s) / U[i, i]

    # Вычисление вектора невязки: r = b - A*x
    # Преобразуем A в array для корректного умножения
    A_array = np.array(A)
    residual = b - np.dot(A_array, x)

    return L, U, x, y, residual


def start(A, b):
    """
    Стартовая функция для совместимости с существующим кодом

    :param A: Исходная матрица
    :param b: Исходный вектор свободных членов
    :return: Возвращает матрицы L, U и векторы x, y
    """
    return solve_system_cholesky(A, b)