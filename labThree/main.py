import matplotlib.pyplot as plt
import numpy as np

def finite_differences(y):
    """Построение таблицы конечных разностей
    :param y - список значений yi = f(xi)
    :return Список списков с конечными разностями
    """
    n = len(y) # кол-во узлов
    diffs = [y.copy()]
    for k in range(1, n):
        prev = diffs[-1]
        curr = [prev[i+1] - prev[i] for i in range(len(prev)-1)]
        diffs.append(curr)
    return diffs

def gauss_second_formula(x, x_nodes, y_nodes):
    """
    Интерполяция по второй формуле Гаусса
    :param x - точка интерполирования xj
    :param x_nodes - узлы интерполяции xi
    :param y_nodes - значения функции yi
    :return Приближенное значении функции Pn(x)
    """
    n = len(x_nodes)
    h = x_nodes[1] - x_nodes[0] # шаг

    i0 = n // 2 - 1 # центральный индекс
    x0 = x_nodes[i0] # значение аргумента
    q = (x - x0) / h
    diffs = finite_differences(y_nodes)
    result = y_nodes[i0] # 1-ый член полинома
    fact = 1
    q_mult = 1 # произв. множ. с q

    for k in range(1, n):
        fact *= k
        if k == 1:
            q_mult *= q
            delta = diffs[1][i0]
        elif k % 2 == 0:
            q_mult *= (q - (k // 2))
            delta = diffs[k][i0 - k // 2]
        else:
            q_mult *= (q + (k // 2))
            delta = diffs[k][i0 - k // 2]

        result += q_mult * delta / fact

    return result
# Исходные данные
xi = [1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]
yi = [0.888551, 0.889599, 0.890637, 0.891667, 0.892687,
     0.893698, 0.894700, 0.895693, 0.896677, 0.897653, 0.898619]
xj = [1.4161, 1.4625, 1.4135, 1.470, 1.41]
print("\t\tВторой метод Гаусса")
print("|\tj\t|\t  xj\t|\t Pn(xj)\t\t|")
print("|-------|-----------|---------------|")
for j in range(len(xj)):
    pn = gauss_second_formula(xj[j], xi, yi)
    print(f"|\t{j + 1}\t|\t{xj[j]:.4f}\t|\t{pn:.6f}\t|")

x_plot = np.linspace(min(xi), max(xi), 400)
y_gauss = [gauss_second_formula(x, xi, yi) for x in x_plot]
plt.figure(figsize=(9, 6))
plt.plot(
    xi, yi,
    'o',
    color='blue',
    markersize=7,
    label='Узлы интерполяции'
)
plt.plot(
    x_plot, y_gauss,
    color='red',
    linewidth=2,
    label='Интерполяция (2-я формула Гаусса)'
)
y_xj_gauss = [gauss_second_formula(x, xi, yi) for x in xj]
plt.scatter(
    xj, y_xj_gauss,
    color='green',
    marker='x',
    s=80,
    linewidths=2,
    zorder=5,
    label='Точки xj'
)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.savefig("interpolation.png", dpi=300, bbox_inches="tight")
plt.close()