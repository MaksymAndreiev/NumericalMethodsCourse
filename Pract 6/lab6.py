import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return (1.5 * np.power(x, 2) + x) / (np.power(x, 5) + 1)


a = 1.2
b = 0

interval = (a - b) / 10
x = [i for i in np.arange(b, a + interval, interval)]
print(f'x: {x}')
y = list(map(func, x))
print(f'y: {y}')

plt.plot(x, y, 'ko')
plt.plot(x, y)
plt.show()

h = interval
print('-' * 5 + 'Метод прямокутників' + '-' * 5)
print(f'h: {h}')
print('I = h * sum(fun(x + h/2))')
I1 = h * sum(map(func, [xi + h / 2 for xi in x[:-1]]))
print(f'I = {I1}')

print('-' * 5 + 'Метод трапецій' + '-' * 5)
print('I = h * ((func(x[0]) + func(x[-1])) / 2 + sum(func(x[1:-1])))')
I2 = h * ((func(x[0]) + func(x[-1])) / 2 + sum(func(x[1:-1])))
print(f'I = {I2}')

print('-' * 5 + 'Метод Сімпсона' + '-' * 5)
print('I = h / 3 * (func(x[0]) + func(x[-1]) + 4 * sum(func([x[2 * i - 1] for i in range(1, int(len(x) / 2) + 1)])) +' +
      '2 * sum(func([x[2 * i] for i in range(1, int((len(x) - 2) / 2) + 1)])))')
I3 = h / 3 * (func(x[0]) + func(x[-1]) + 4 * sum(func([x[2 * i - 1] for i in range(1, int(len(x) / 2) + 1)])) +
              2 * sum(func([x[2 * i] for i in range(1, int((len(x) - 2) / 2) + 1)])))
print(f'I = {I3}')
