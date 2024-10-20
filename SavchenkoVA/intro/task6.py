"""
Задача 6:
На ввод подаются N целых чисел, их нужно сохранить в массив или список.
Затем вывести максимальный элемент.

Пример ввода:
5
2
3
56
45
21

Пример вывода:
56
"""


def task6() -> None:
    n = int(input('Введите количество чисел: '))
    k = list()
    for i in range(n):
        k.append(int(input('Введите число: ')))
    print('Результат:', max(k))


"""
Задача 6*:
Сначала на вход поступает длина последовательности N.
Затем элементы последовательности – целые числа. Напишите программу,
которая подсчитывает количество положительных чисел среди элементов последовательности.

Пример ввода:
5
1
2
3
-1
-4

Пример вывода:
3
"""


def task6_p() -> None:
    n = int(input('Введите количество чисел: '))
    k = 0
    for i in range(n):
        if int(input('Введите число: ')) > 0:
            k += 1
    print('Результат:', k)


if __name__ == "__main__":
    print('Задача 6:')
    task6()
    print('\nЗадача 6*:')
    task6_p()
