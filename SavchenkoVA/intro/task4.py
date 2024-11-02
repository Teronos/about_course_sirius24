"""
Задача 4:
Вводится натуральное число N, а затем N целых чисел последовательности.
Найдите количество минимальных элементов в последовательности.

Пример ввода:
3
21
11
4

Пример вывода:
1
"""


def task4() -> None:
    n = int(input('Введите количество чисел: '))
    k = 1
    m = int(input('Введите число: '))
    min_m = m
    for i in range(n - 1):
        m = int(input('Введите число: '))
        if m < min_m:
            min_m = m
            k = 1
        elif m == min_m:
            k += 1
    print('Результат:', k)


"""
Задача 4*:
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что  φ_n=A . Если А не является числом Фибоначчи, выведите число -1.

Пример ввода:
8

Пример вывода:
6
"""


def task4_p() -> None:
    a = int(input('Введите число: '))
    x = 0
    y = 1
    k = 0
    while y <= a:
        t = x + y
        x = y
        y = t
        k += 1
    print('Результат:', k if (x == a) else '-1')


if __name__ == "__main__":
    print('Задача 4:')
    task4()
    print('\nЗадача 4*:')
    task4_p()