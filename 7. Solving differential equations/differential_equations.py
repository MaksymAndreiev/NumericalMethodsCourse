import numpy as np
from matplotlib import pyplot as plt


def derivative(x, y):
    # return y*(x - 1) - (2 - 0.5 * x) * x
    return np.power((x + y), 2) + 0.5 * (x + y)


h = 0.05
x0 = 0
y0 = 0
# y0 = 1
print('Початкова умова: y({}) = {}'.format(x0, y0))
print('Крок h = {}'.format(h))
print('Діапазон [{}, {}]'.format(y0, y0 + 2))

print('\nРозіб\'ємо вихідний інтервал [{}, {}] на однакові відрізки з кроком h = {}.'.format(y0, y0 + 2, h))
x = [round(i, 2) for i in np.arange(x0, y0 + 2 + h, h)]
print(x)

print()
print('-' * 10 + 'Розв’язання задачі Коши методом Ейлера' + '-' * 10)
print(f'Знаходимо значення функції за початкової умови у({x0}) = {y0} f(хi, yi) = {derivative(x0, y0)}')
y = [y0]


def get_y(i):
    xi = x[i]
    yi = y[i]
    new_y = round(yi + h * derivative(xi, yi), i + 5)
    y.append(new_y)
    return new_y


[get_y(i) for i in range(len(x) - 1)]
print(y)

print()
print('-' * 10 + 'Розв’язання задачі Коши методом Рунге-Кутта' + '-' * 10)


def k1(x, y):
    return derivative(x, y)


def k2(x, y):
    return derivative(x + h / 2, y + h / 2 * k1(x, y))


def k3(x, y):
    return derivative(x + h / 2, y + h / 2 * k2(x, y))


def k4(x, y):
    return derivative(x + h, y + h * k3(x, y))


y2 = [y0]


def get_y2(i):
    xi = x[i]
    yi = y2[i]
    new_y = round(yi + h / 6 * (k1(xi, yi) + 2 * k2(xi, yi) + 2 * k3(xi, yi) + k4(xi, yi)), i + 5)
    y2.append(new_y)
    return new_y


print(
    f'Знаходимо значення функції за початкової умови у({x0}) = {y0} k1 = {k1(x0, y0)}, k2 = {k2(x0, y0)}, k3 = {k3(x0, y0)}, k4 = {k4(x0, y0)}')
[get_y2(i) for i in range(len(x) - 1)]
print(y2)

plt.plot(x, y, 'bo')
plt.plot(x, y, label="Метод Ейлера")
plt.plot(x, y2, 'ro')
plt.plot(x, y2, 'r', label="Метод Рунге-Кутта")
plt.legend()
plt.suptitle('Розв’язання диференційних рівнянь')
plt.show()
