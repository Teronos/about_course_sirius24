# 7
# Напишите программу, которая в последовательности чисел находит сумму двузначных чисел,
# кратных 8. Программа в первой строке получает на вход число n - количество чисел в
# последовательности, во второй строке -- n чисел, входящих в данную последовательность.
def print_sum_of_two_digit_numbers_from_sequence() -> int:
    count_num = int(input())

    nums = input().split(' ')

    nums_div_each = [int(i) for i in nums[:count_num] if int(i) % 8 == 0 and (100 > int(i) > 10)]

    return sum(nums_div_each)

# 7*
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.
def get_count_biggest_num_in_sequences() -> int:
    target_num = int(input())
    max_num = target_num
    max_num_repeat_count = 0

    while target_num != 0:
        if target_num > max_num:
            max_num = target_num
            max_num_repeat_count = 0

        if target_num == max_num:
            max_num_repeat_count = max_num_repeat_count + 1

        target_num = int(input())

    return max_num_repeat_count