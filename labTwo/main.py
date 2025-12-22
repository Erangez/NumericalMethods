import algorithm
import numpy as np

if __name__ == "__main__":
    A = np.matrix([
        [0.49, 0, -0.128, 0.09, 0.15],
        [-0.03, 0.32, 0, -0.061, 0.02],
        [0.01, -0.09, 0.58, 0.011, 0.035],
        [0.03, 0, -0.073, 0.58, 0],
        [0.02, -0.03, 0.145, -0.012, 0.42]
    ])
    b = np.array([0.964, 1.279, -1.799, -4.971, 2.153])

    L, U, x, y, residual = algorithm.solve_system_cholesky(A, b)

    print(f"""
    --------------- Метод Холецкого ---------------
Входные данные:
    Матрица A:
{A}
    Вектор b: {b}

Результаты:
    Решение x: {[float(round(n, 6)) for n in x]}
    Промежуточный вектор y: {[float(round(n, 6)) for n in y]}
    Вектор невязки r = b - A*x: {[float(round(float(n), 10)) for n in residual]}
    Норма вектора невязки ||r||: {np.linalg.norm(residual):.10f}

Матрицы LU-разложения:
    Нижняя треугольная матрица L:
{np.round(L, 6)}
    Верхняя треугольная матрица U:
{np.round(U, 6)}

Проверка решения:
    A*x = {np.dot(np.array(A), x).round(6)}
    b = {b.round(6)}
    Совпадение: {np.allclose(np.dot(np.array(A), x), b, rtol=1e-9)}
    """)