import matplotlib.pyplot as plt
from math import sqrt, pi, exp

x0 = 1.0
b = 6.0
y0 = 10.0
h0 = 0.5
eps = 1e-3

# функции варианта
def g(x):
    return 2 * (x - 2)

def phi(x):
    return (x + 2) * exp(-x**2)

def psi(x):
    return 1 / sqrt(2 * pi)

def F(x):
    return phi(x) * psi(x)

def f(x, y):
    return F(x) - g(x) * y

# Метод Рунге–Кутта 2 порядка
def rk2_step(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    return y + k2

# автоматический выбор шага
x = x0
y = y0
h = h0

xs_adapt = [x]
ys_adapt = [y]

while x < b:
    if x + h > b:
        h = b - x

    y_h = rk2_step(x, y, h)
    y_half = rk2_step(x, y, h / 2)
    y_h2 = rk2_step(x + h / 2, y_half, h / 2)

    delta = abs(y_h - y_h2) / 3

    if delta > eps:
        h /= 2
        continue
    else:
        x += h
        y = y_h2
        xs_adapt.append(x)
        ys_adapt.append(y)

        if delta < eps / 8:
            h *= 2

N = len(xs_adapt) - 1

# таблица с автошагом
print("\nТАБЛИЦА 1 — Метод Рунге–Кутта 2-го порядка")
print("Автоматический выбор шага")
print("-" * 50)
print(f"{'k':>3} {'x_k':>12} {'y_k':>18}")
print("-" * 50)

for i, (xi, yi) in enumerate(zip(xs_adapt, ys_adapt)):
    print(f"{i:3d} {xi:12.6f} {yi:18.8f}")

# график с автошагом
plt.figure()
plt.plot(xs_adapt, ys_adapt, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Рунге–Кутта 2 порядка (автоматический шаг)")
plt.grid()
plt.savefig("rk2_adaptive.png")
plt.close()

# постоянный шаг
h_fixed = (b - x0) / N

xs_fixed = [x0]
ys_fixed = [y0]

x = x0
y = y0

for _ in range(N):
    y = rk2_step(x, y, h_fixed)
    x += h_fixed
    xs_fixed.append(x)
    ys_fixed.append(y)

# таблица постоянного шага
print("\nТАБЛИЦА 2 — Метод Рунге–Кутта 2-го порядка")
print("Постоянный шаг")
print("-" * 50)
print(f"{'k':>3} {'x_k':>12} {'y_k':>18}")
print("-" * 50)

for i, (xi, yi) in enumerate(zip(xs_fixed, ys_fixed)):
    print(f"{i:3d} {xi:12.6f} {yi:18.8f}")

# график с постоянным шагом
plt.figure()
plt.plot(xs_fixed, ys_fixed, marker='s')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Рунге–Кутта 2 порядка (постоянный шаг)")
plt.grid()
plt.savefig("rk2_fixed.png")
plt.close()

print(f"Число шагов N = {N}")
print("Файлы графиков сохранены:")
print(" - rk2_adaptive.png - Автоматический")
print(" - rk2_fixed.png - Постоянный")