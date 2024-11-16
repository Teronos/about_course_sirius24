# Напишите функцию my_sort, которая принимает двумерный массив n x n, а возвращает элементы массива,
# расположенные от самых крайних элементов до среднего элемента, таким образом, чтобы происходило перемещение по часовой стрелке.

import random


def my_sort(array) -> list:
    res = []
    length = len(array)
    row = 0
    column = 0
    leftBound = 0

    while length > 1:
        # ряд слева направо
        while column < length:
            res.append(array[row][column])
            column += 1

        # последний столбец
        row += 1
        column -= 1
        while row < length:
            res.append(array[row][column])
            row += 1

        # последняя строка наоборот
        row -= 1
        column -= 1
        while column >= leftBound:
            res.append(array[row][column])
            column -= 1

        leftBound += 1
        length -= 1

        if length >= 2:
            # подняться наверх
            row -= 1
            column += 1
            while row >= leftBound:
                res.append(array[row][column])
                row -= 1

            row = leftBound
            column = leftBound

    return res


size = int(input("Введите размер массива n*n: "))
array2 = []
for i in range(0, size):
    array1 = []
    for j in range(0, size):
        array1.append(random.randrange(0, 100))
    array2.append(array1)
print(array2)

print(my_sort(array2))
