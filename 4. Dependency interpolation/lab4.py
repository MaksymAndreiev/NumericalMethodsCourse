import numpy as np
import sympy
import matplotlib.pyplot as plt

X_array = [int(i) for i in input('Ввведіть значення х через пробіл: ').split(' ')]
Y_array = [round(float(i), 1) for i in input('Ввведіть значення у через пробіл: ').split(' ')]
index = X_array.index(X_array[-1])
print('-' * 10 + ' Інтерполяція методом полінома Лагранжа ' + '-' * 10)
print(f'Поліном Лагранжа буде {index}-го ступеня.')

x = sympy.symbols('x')
p = [0 for i in range(index + 1)]

for i in range(len(X_array)):
    a = 1
    for j in range(len(X_array)):
        if i != j:
            pp = (x - X_array[j]) / (X_array[i] - X_array[j])
            a *= pp
    p[i] = a

Ln = [Y_array[i] * p[i] for i in range(index + 1)]
Ln = sum(Ln)
print(Ln)
print(sympy.expand(Ln))

Ln_coef = []
for i in range(index + 1):
    Ln_coef.append(round(sympy.expand(Ln).coeff(x, i), 3))

print(f'Коефіцієнти: {Ln_coef[::-1]}')

X = np.linspace(3, 7, 50)
l = sympy.lambdify(x, Ln, modules=['numpy'])
Y = l(X)

plt.plot(X_array, Y_array, 'ko')
plt.plot(X, Y)
plt.title('Інтерполяція методом полінома Лагранжа')
plt.show()
