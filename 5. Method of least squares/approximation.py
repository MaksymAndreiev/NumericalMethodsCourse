import numpy as np
import sympy
import matplotlib.pyplot as plt

X_array = [int(i) for i in input('Ввведіть значення х через пробіл: ').split(' ')]
Y_array = [round(float(i), 1) for i in input('Ввведіть значення у через пробіл: ').split(' ')]
index = X_array.index(X_array[-1])

print('-' * 10 + ' Апроксимація методом найменших квадратів ' + '-' * 10)
print('Виконаємо наближення поліномом першого ступеня:\nP1(x) = ax+ b')
x_sum = sum(X_array)
y_sum = sum(Y_array)
x2_sum = sum(np.power(X_array, 2))
xy_sum = np.round(sum(np.multiply(X_array, Y_array)), 4)

a, b = sympy.symbols('a b')
print('Коефіціенти a та b розраховуємо за формулами:')
print(f'{a * x_sum + b * len(X_array)} = {y_sum}')
print(f'{a * x2_sum + b * x_sum} = {xy_sum}')

aa, bb = list(sympy.linsolve([a * x_sum + b * len(X_array) - y_sum, a * x2_sum + b * x_sum - xy_sum],
                             (a, b)))[0]
aa, bb = round(aa, 2), round(bb, 2)
print('Знаходимо значення коефіціентів та формуємо поліном першого ступеня:')
print(f'P1(x)={aa}x+{bb}')
Px = aa * x + bb
X = np.linspace(3, 7, 50)
X_array = np.array(X_array)
Y_array = np.array(Y_array)
l = sympy.lambdify(x, Px, modules=['numpy'])
Y = l(X)
P1 = l(X_array)
J1 = round(sum(np.power(Y_array - P1, 2)), 2)
print(f'Відхилення у методі найменших квадратів: {J1}')

plt.subplot(1, 2, 1)
plt.plot(X_array, Y_array, 'ko')
plt.plot(X, Y)

print('Виконаємо наближення поліномом другого ступеня:\nP2(x) = ax^2 + bx + c')
x3_sum = sum(np.power(X_array, 3))
x4_sum = sum(np.power(X_array, 4))
x2y_sum = sum(np.power(X_array, 2) * Y_array)
c = sympy.symbols('c')

print('Коефіціенти a, b та c розраховуємо за формулами:')
print(f'{a * x2_sum + b * x_sum + c * len(X_array)} = {y_sum}')
print(f'{a * x3_sum + b * x2_sum + c * x_sum} = {xy_sum}')
print(f'{a * x4_sum + b * x3_sum + c * x2_sum} = {x2y_sum}')

aa, bb, cc = \
    list(
        sympy.linsolve([a * x2_sum + b * x_sum + c * len(X_array) - y_sum,
                        a * x3_sum + b * x2_sum + c * x_sum - xy_sum,
                        a * x4_sum + b * x3_sum + c * x2_sum - x2y_sum], (a, b, c)))[0]
aa = round(aa, 2)
bb = round(bb, 2)
cc = round(cc, 2)
print('Знаходимо значення коефіціентів та формуємо поліном другого ступеня:')
print(f'P2(x)={aa}x^2 + {bb}x + {cc}')
Px = aa * x * x + bb * x + cc
l = sympy.lambdify(x, Px, modules=['numpy'])
Y = l(X)
P2 = l(X_array)
J2 = round(sum(np.power(Y_array - P2, 2)), 2)
print(f'Відхилення у методі найменших квадратів: {J2}')

plt.subplot(1, 2, 2)
plt.plot(X_array, Y_array, 'ko')
plt.plot(X, Y)
plt.suptitle('Апроксимація методом найменших квадратів')
plt.show()

print(f'Маємо два значення сум квадратів похибок поліномів P1(x) та P2(X):\n{J1} та {J2}')
if J1 > J2:
    print('Після порівняння результатів, бачимо, що поліном другого ступеня має значно кращий результат.')
else:
    print('Після порівняння результатів, бачимо, що поліном першого ступеня має значно кращий результат.')
