from typing import List

# 8
# Даны два числа. Определить цифры, входящие в запись как первого, так и второго числа.
# Программа должна вывести цифры, которые имеются в обоих числах, через пробел.
# Цифры выводятся в порядке их нахождения в первом числе.
def get_common_digits(num1: int, num2: int) -> str:
    return " ".join([digit for digit in str(num1) if digit in str(num2)])

# 8*
# Напишите функцию my_sort, которая принимает двумерный массив n x n, а возвращает элементы массива,
# расположенные от самых крайних элементов до среднего элемента, таким образом, чтобы происходило
# перемещение по часовой стрелке.
def my_sort(matrix: List[List[int]]) -> List[int]:
    result = []
    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result