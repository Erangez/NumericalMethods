import numpy as np
import matplotlib.pyplot as plt

def graph1(ax):
    # Визуал
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.minorticks_on()
    ax.grid(which="major")
    ax.grid(which="minor", linestyle=":")
    x1 = np.arange(-1, 1, 0.001)
    y1 = np.sqrt(1 - x1 ** 2) - 4 * x1 ** 5 + x1
    x2 = np.arange(0, 1, 0.001)
    y2 = x2
    ax.plot(x1, y1, color="blue", label="g(x) = √(1 - x²) - 4x⁵ + x")
    ax.plot(x2, y2, color="orange", label = "y = x")

    # Функция и производные
    # fx = np.sqrt(1 - x**2) - 4 * x**5
    # gx = np.sqrt(1 - x**2) - 4 * x**5 + x
    # g'x = -x/np.sqrt(1 - x**2) - 20 * x**4 + 1

    # Получение значения функции или производных
    def get_function_value(x, i):
        if i == 0:
            return np.sqrt(1 - x**2) - 4 * x**5             #f(x)
        elif i == 1:
            return np.sqrt(1 - x**2) - 4 * x**5 + x         #g(x)
        elif i == 2:
            return -x/np.sqrt(1 - x**2) - 20 * x**4 + 1     #g'(x)

    e = 0.001
    toRoundInt = int(f"{e:e}"[-1])
    print("-" * 30)
    print("Метод простых итераций:")
    print("Графически видно, что единственный корень определён на отрезке [0.6, 0.8]")
    a, b = 0.6, 0.8
    print("Проверим условие сходимости |g'(x)| < 1")
    # Проверка условия сходимости
    x_range = np.arange(a, b + e, e)
    derivative_values = [abs(get_function_value(x, 2)) for x in x_range]
    max_derivative = max(derivative_values)
    min_derivative = min(derivative_values)

    print(f"Минимальное значение |g'(x)| на отрезке: {min_derivative:.6f}")
    print(f"Максимальное значение |g'(x)| на отрезке: {max_derivative:.6f}")

    # Визуализация итерационного процесса
    x0 = (a+b)/2
    iterations = 100
    current_x = x0
    first_iteration = False
    print("Начальное приближение: x₀ = ", round(current_x, toRoundInt))
    ax.text(current_x, 0, f'x={round(current_x, toRoundInt)}', font="Times New Roman", fontsize=10,
            rotation=45, color="black")
    ax.scatter(current_x,0, marker='o', s=15, color="black", label="Начальная точка")
    ax.plot([current_x, current_x], [0, get_function_value(current_x, 1)], 'gray', linestyle=':', alpha=0.5, label="Проекция на g(x)")
    # print("Итерации:")
    ax.plot(0, 0, "r--", label="Итерации")
    for i in range(iterations):
        next_x = get_function_value(current_x, 1)  # g(x)
        if not first_iteration:
            ax.arrow(current_x, next_x, next_x - current_x, 0,
                     head_width=0.008, head_length=0.01,
                     fc='red', ec='red', linestyle='--', alpha=0.7, length_includes_head=True)
            first_iteration = True
        else:
            ax.arrow(current_x, current_x, 0, next_x - current_x,
                     head_width=0.008, head_length=0.01,
                     fc='red', ec='red', linestyle='--', alpha=0.7, length_includes_head=True)
            ax.arrow(current_x, next_x, next_x - current_x, 0,
                     head_width=0.008, head_length=0.01,
                     fc='red', ec='red', linestyle='--', alpha=0.7, length_includes_head=True)
        print(f"Итерация {i + 1}: xᵢ = {current_x:.{toRoundInt}f} → g(x) = {next_x:.{toRoundInt}f}")
        if abs(next_x - current_x) < e:
            current_x = next_x
            break
        current_x = next_x

        # Проверка на выход за пределы или расхождение
        if current_x < -1 or current_x > 1.0 or np.isnan(current_x):
            print("Процесс расходится")
            break
        else:
            ax.plot([current_x, current_x], [0, next_x], 'green', linestyle=':', alpha=0.5, label="Проекция на Ox")
            ax.text(next_x, 0, f'x={i+1}', font="Times New Roman", fontsize=10,
                     rotation=45, color="green")
    if min_derivative < 1:
        print("\nРезультат:")
        print("Ответ:", current_x)
        iterationsAmount = i + 1
        print(f"Количество итераций: {iterationsAmount}")
    else:
        print(f"\nУсловие сходимости не выполнено")
        print(f"min|g'(x)| = {min_derivative:.6f} ≥ 1")
        print("Метод простых итераций расходится")
        iterationsAmount = i + 1

    ax.legend(loc="best")
    ax.set_title("Метод простых итераций", fontsize=10)

    return ax

def graph2(ax):
    # Визуал
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.minorticks_on()
    ax.grid(which="major")
    ax.grid(which="minor", linestyle=":")
    x1 = np.arange(-1, 1, 0.001)
    y1 = np.sqrt(1 - x1**2) - 4 * x1**5
    ax.plot(x1,y1, color="blue", label = "y = f(x) = √(1 - x²) - 4x⁵")

    # Функция и производные
    # fx = math.sqrt(1 - x**2) - 4 * x**5
    # f'x = -x/(math.sqrt(1-x**2)) - 20*x**4
    # f"x = (-1/(math.sqrt(1-x**2) * (1-x**2))) - 80*x**3

    # Функция для построения касательной
    def tangent_line(x, x0):
        fx = np.sqrt(1 - x0**2) - 4 * x0**5
        f1x = -x0 / (np.sqrt(1 - x0**2)) - 20 * x0**4
        return fx + f1x * (x - x0)

    # Получение значения функции или производных
    def get_function_value(x, i):
        if i == 0: return np.sqrt(1 - x**2) - 4 * x**5                  #f(x)
        elif i == 1: return -x/(np.sqrt(1-x**2)) - 20*x**4              #f'(x)
        elif i == 2: return -1/(np.sqrt(1-x**2) * (1-x**2)) - 80*x**3   #f''(x)
    e = 0.001
    toRoundInt = int(f"{e:e}"[-1])
    iterationsAmount = 1
    iterations_history = []
    print("-" * 30)
    print("Модифицированный метод Ньютона:")
    a, b = 0.6, 0.8
    print("Графически видно, что единственный корень определён на отрезке [0.6, 0.8]")
    print("Найдём начальное значение корня в этом отрезке используя неравенство: f(x₀) * f''(x₀) > 0")
    print("Проверим с помощью неравенства f(a)f(b) < 0 выбранный отрезок:")
    print(f"f(a) = {get_function_value(a, 0)}")
    print(f"f(b) = {get_function_value(b, 0)}")
    print("f(a)f(b) < 0 ? -", get_function_value(a, 0) * get_function_value(b, 0) < 0)
    print("\nНайдём начальное значение корня: ")
    print("Значение f''(x) на отрезке < 0, а значит нам нужен f(b), b = 0.8")
    print("Значит x₀ = b = 0.8")
    x0 = b
    print("Полученный наиболее подходящий корень:", round(x0, toRoundInt))
    ax.scatter(x0,0, marker='o', s=15, color="black", label="Начальная точка")
    ax.text(x0, 0, f'x={round(x0, toRoundInt)}', font="Times New Roman", fontsize=10,
            rotation=45, color="black")


    print(f"{'Итерация':<10} {'x₀':<12} {'f(x₀)':<12} {'f1(x₀)':<12} {'x₁':<12}")
    f1x = -x0 / (np.sqrt(1 - x0 ** 2)) - 20 * x0 ** 4
    x_tangent = np.linspace(x0 - 0.2, x0 + 0.2, 50)
    y_tangent = [tangent_line(x, x0) for x in x_tangent]
    ax.plot(x_tangent, y_tangent, '--', alpha=0.7, linewidth=1, color="red", label="Начальная касательная")
    tangent_line_plotted = False
    vertical_line_plotted = False
    while True:
        fx = get_function_value(x0, 0)
        h = fx / f1x
        x1 = x0 - h
        iterations_history.append((x0, fx, f1x, x1))
        print(f"{iterationsAmount:<10} {x0:<12.{toRoundInt}f} {fx:<12.{toRoundInt}f} {f1x:<12.{toRoundInt}f} {x1:<12.{toRoundInt}f}")

        ax.plot([x0, x0], [0, fx], 'gray', linestyle=':', alpha=0.5,
                label="Проекция на функцию" if not vertical_line_plotted else "")
        vertical_line_plotted = True
        ax.plot(x0, fx, 'ro', markersize=4, label="Точка проекции" if iterationsAmount == 1 else "")
        ax.plot([x0, x1], [fx, 0], 'r-', alpha=0.7, linewidth=1,
                label="Касательная к корню" if not tangent_line_plotted else "")
        tangent_line_plotted = True
        ax.plot(x1, 0, color="brown", markersize=4)

        if abs(h) < e:
            ax.plot(x1, 0, 'o', color="green", markersize=6, label='Найденный корень')
            break

        x0 = x1
        iterationsAmount += 1
    ax.text(x1, 0, f'x={round(x1, toRoundInt)}', font="Times New Roman", fontsize=10,
            rotation=45, color="green")
    x1 = round(x1, toRoundInt)
    print("\nРезультат:")
    print("Ответ:", x1)
    print("Количество итераций:", iterationsAmount)
    print("-" * 50)
    ax.legend(loc="best")
    ax.set_title("Модифицированный метод Ньютона", fontsize=10)
    return ax

if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2)
    graph1(axes[0])
    graph2(axes[1])
    fig.suptitle("Лабораторная работа №1", font="Times New Roman", fontsize=14, fontweight="bold")
    plt.show()