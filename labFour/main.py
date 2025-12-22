import math
import matplotlib.pyplot as plt

# узлы и коэффициенты Гаусса, n = 4
t_nodes = [-0.86113631, -0.33998104, 0.33998104, 0.86113631]
A = [0.34785484, 0.65214516, 0.65214516, 0.34785484]

# квадратурная формула Гаусса
def gauss_integral(f, a, b):
    s = 0.0
    for ti, Ai in zip(t_nodes, A):
        x = (a + b) / 2 + (b - a) / 2 * ti
        s += Ai * f(x)
    return (b - a) / 2 * s

# функция f1(x)
def f1(x):
    return math.tan(x / 2 + math.pi / 4) ** 3

# интеграл u
a1 = 0
b1 = math.pi / 4
u = gauss_integral(f1, a1, b1)

print("Значение интеграла u:")
print(f"u = {u:.6f}\n")

# функции φ(z), ψ(x), f2(x,t)
mu = 0.01

def phi(z):
    return math.sqrt(math.pi - math.atan(z))

def psi(x):
    return math.sqrt(x * x + 1) / (x * x + 3)

# вычисление F(t)
a2 = 0
b2 = 1
c = 1
d = 2
m = 20

h = (d - c) / m

t_values = []
F_values = []

print("Таблица значений F(t):")
print(" i     t_i        F(t_i)")
print("--------------------------------")

for i in range(m + 1):
    t = c + i * h

    z = a2 + (b2 - a2) * (c * t + d) / m

    Ft = gauss_integral(
        lambda x: phi(t / (1 + x * x) + mu * x) * psi(x),
        a2,
        b2
    )

    t_values.append(t)
    F_values.append(Ft)

    print(f"{i:2d}   {t:6.3f}    {Ft: .6f}")
# график
plt.figure()
plt.plot(t_values, F_values, marker='o')
plt.xlabel("t")
plt.ylabel("F(t)")
plt.title("График функции F(t)")
plt.grid(True)
plt.savefig("4.png", dpi=300, bbox_inches="tight")
plt.close()