"""
Задача 8:
Даны два числа. Определить цифры, входящие в запись как первого, так и второго числа.
Программа должна вывести цифры, которые имеются в обоих числах, через пробел.
Цифры выводятся в порядке их нахождения в первом числе.

Пример ввода:
564 8954

Пример вывода:
5 4
"""


def task8():
    n, m = input('Введите два числа: ').split(' ')
    print('Результат:', end=' ')
    for i in n:
        if i in m:
            print(i, end=' ')
    print()


"""
Задача 8*:
Напишите функцию my_sort, которая принимает двумерный массив n x n,
а возвращает элементы массива, расположенные от самых крайних элементов до среднего элемента,
таким образом, чтобы происходило перемещение по часовой стрелке.

То есть функция должна преобразовывать array = [ [1,2,3], [4,5,6], [7,8,9] ]

my_sort(array) #=> [1,2,3,6,9,8,7,4,5]

Еще один пример работы функции:

array = [ [1,2,3], [8,9,4], [7,6,5] ] my_sort(array) #=> [1,2,3,4,5,6,7,8,9]
"""


def my_sort(array):
    result = list()
    start_rows = 0
    start_columns = 0
    finish_rows = len(array) - 1
    finish_columns = len(array[0]) - 1
    while start_rows <= finish_rows and start_columns <= finish_columns:
        for i in range(start_columns, finish_columns + 1):
            result.append(array[start_rows][i])
        start_rows += 1
        for i in range(start_rows, finish_rows + 1):
            result.append(array[i][finish_columns])
        finish_columns -= 1
        if start_rows <= finish_rows:
            for i in range(finish_columns, start_columns - 1, -1):
                result.append(array[finish_rows][i])
            finish_rows -= 1
        if start_columns <= finish_columns:
            for i in range(finish_rows, start_rows - 1, -1):
                result.append(array[i][start_columns])
            start_columns += 1
    return result


def task8_p():
    array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Результат сортировки массива:', array1, '=', my_sort(array1))
    array2 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print('Результат сортировки массива:', array2, '=', my_sort(array2))


if __name__ == "__main__":
    print('Задача 8:')
    task8()
    print('\nЗадача 8*:')
    task8_p()
