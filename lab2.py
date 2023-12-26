import numpy as np

eps = 0.005
m = 1

a = np.array([
    [5, 1, -1, 1],
    [1, -4, 1, -1],
    [-1, 1, 4, 1],
    [1, 2, 1, -5]
], dtype=float)
print('Коефіцієнти системи рівняннь:\n', a)

l1 = range(len(a))
l2 = range(len(a[0]))

detA = np.linalg.det(a)
print('Визначник: ', detA)

b = np.array([3 * m, m - 6, 15 - m, m + 2])
print('Вектор відповідей системи рівняннь:\n', b)

x = []
x0 = np.array([0.7 * m, 1, 2, 0.5])
x.append(x0)

s = [sum(abs(a[i][j]) for j in l2 if i != j) for i in l1]
d = [abs(a[i][j]) for i in l1 for j in l2 if i == j]
print('Виконнання умов збіжності: ', s < d)

print('=' * 60)
e = 100
k = 0
while e > eps:
    if k > 1:
        e = max(np.round(abs(x[k] - x[k - 1]), 5))
        print('Точність: ', e)
    if e <= eps:
        break
    x_ = np.array([round((b[i] - sum(a[i][j] * x[k][j] for j in l2 if j != i)) / a[i][i], 3) for i in l1])
    print(f'Виконуємо {k + 1}-ту ітерацію:', x_)
    x.append(x_)
    k += 1

print('=' * 60)
print(f'Результат {k}-ої ітерації: ', x[-1])
check = np.inner(x[-1], a)
print('Перевірка: ', check)
print('Пройшло перевірку: ', b == np.round(check))
