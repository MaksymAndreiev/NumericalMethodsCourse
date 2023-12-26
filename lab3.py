import numpy as np


def function(x: int or float) -> float:
    return 2.1 * pow(x, 3) + 1.4 * pow(x, 2) - 4.3 * x + 6.1


def find_x(a, b):
    global j
    a = round(a, j + 1)
    b = round(b, j + 1)
    c = (a + b) / 2
    c = round(c, j + 1)
    j += 1
    if round(function(c), 3) == 0:
        print(c)
        print('Знаходимо значення функції:', round(function(c), 3))
        print('Пройшло перевірку.')
        return round(c, j)
    else:
        print(f'Розглядаємо інтервал [{a}, {b}]')
        print(f'Корінь на ітерації {j - 1} : {c}')
        if np.sign(function(a)) != np.sign(function(c)):
            print('Знаки функцій \033[1;31mрізні\033[0m: {}, {}'.format(round(function(a), j - 1),
                                                                        round(function(b), j - 1)))
            b = c
        else:
            print('Знаки функцій \033[1;33mоднакові\033[0m: {}, {}'.format(round(function(a), j - 1),
                                                                           round(function(b), j - 1)))
            a = c
        print('Використовуємо середнє значення діапазону як нову межу уточнених діапазонів.')
        if abs(b - a) < 2 * eps:
            mod = round(abs(b - a), j - 1)
            print('Досягнено потрібної точності.')
            print(f'|b - a| < 2 * eps: {mod} < {2 * eps}')
            print('Знаходимо значення кореня: ')
            return find_x(a, b)
        else:
            return find_x(a, b)


x = np.round(np.arange(-6, 6, 0.1, dtype=float), 1)
eps = 0.0001
ranges = list()
eps_ = np.inf

print('Виділяємо ті інтервали, на кінцях яких функція має різні знаки.')
for i in range(len(x) - 1):
    if np.sign(function(x[i])) != np.sign(function(x[i + 1])):
        a = x[i]
        b = x[i + 1]
        ranges.append([a, b])
        print(f'[{a}; {b}] - шуканий інтервал.\n'
              f'Значення функції у ньому: {round(function(a), 3)}, {round(function(b), 3)}.')

for range_ in ranges:
    print('-' * 75)
    print(f'Розглянемо інтервал {range_}:')
    j = 1
    find_x(*range_)
