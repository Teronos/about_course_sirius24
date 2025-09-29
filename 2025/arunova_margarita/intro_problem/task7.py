"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

Пример ввода:
1
3
3
1
0

Пример вывода:
2
"""

max_elem, max_elem_count = None, 0
while True:
    num = int(input())
    if num == 0:
        break

    if max_elem is None or num > max_elem:
        max_elem, max_elem_count = num, 1
    elif num == max_elem:
        max_elem_count += 1

print("Количество элементов: ", max_elem_count)
