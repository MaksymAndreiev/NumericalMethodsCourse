import numpy as np

A = []
while True:
    line = input('A:\n')
    if line == '':
        break
    else:
        line = line.split(' ')
    A.append(line)
A = np.array([float(a) for line in A for a in line])
n = int(np.sqrt(A.size))
A = np.reshape(A, (n, n))
# A = np.array([[4.42, 12.6, 5.77], [0.16, 3.82, 6.41], [7.14, 4.98, 8.73]])
if A.shape[0] != A.shape[1]:
    print('Матриця повинна бути квадратною.')
    n = 0
    exit(0)
else:
    n = A.shape[0]

B = np.array([float(b) for b in input('B:\n').split(' ')])[:, None]
# B = np.array([1.56, 4.42, -2.67])[:, None]
system = np.hstack((A, B))
print('Система рівняннь\n', system)
determinant = np.linalg.det(A)
if determinant != 0:
    print('\nСистема має єдиний розв\'язок.')

# прямий хід
for i in range(n):
    if system[i, i] != 0:
        print(f'\nДілимо {i + 1}-й рядок на {system[i, i]}')
        system[i] /= system[i, i]  # для отримання 1 на діагоналі
    print(system, '\n')
    for j in range(i + 1, n):
        print(f'Від {j + 1}-го рядка віднімаємо {i + 1}-й рядок, помножений на {system[j, i]}')
        system[j] -= system[i] * system[j, i]
    if i != n - 1:
        print(system)

# обратний хід
# print('-' * 18 + ' Обратний хід ' + '-' * 18)
for i in range(2, n + 1):
    for j in range(1, i):
        print(f'Від {n - i + 1}-го рядка віднімаємо {n - i + j + 1}-й рядок, помножений на {system[-i, -i + j - 1]}')
        system[-i] -= system[-i + j] * system[-i, -i + j - 1]
        # -2 -= -1 * [-2 -2]
        # -3 -= -2 * [-3 -3]
        # -3 -= -3 * [-3 -2]

print(system)

X = system[:, -1]

print("\nРозв'язок системи рівняннь: ", X)

print('Перевірка: ', np.dot(A, X))
print(np.round(np.dot(A, X), 2) == B.T)

# system[0] /= A[0, 0]
# print(system)
# for i in range(1, n):
#     system[i] -= system[0]*system[i, 0]
# print(system)
# system[1] /= system[1, 1]
# print(system)
# for i in range(2, n):
#     system[i] -= system[1]*system[i, 1]
# print(system)
