# 6
# На ввод подаются N целых чисел, их нужно сохранить в массив или список.
# Затем вывести макимальный элемент.
def print_max_elem_from_list() -> int:
    el_count = int(input())

    result_list = []

    for _ in range(el_count):
        result_list.append(int(input()))

    return max(result_list)

# 6*
# Сначала на вход поступает длина последовательности N.
# Затем элементы последовательности – целые числа.
# Напишите программу, которая подсчитывает количество положительных чисел среди элементов
# последовательности.
def count_of_positive_numbers_from_sequence() -> int:
    num_count = int(input())
    result = 0

    for _ in range(num_count):
        if int(input()) > 0:
            result += 1

    return result