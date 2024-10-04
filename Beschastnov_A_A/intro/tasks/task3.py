# Задача 3
# Вводится натуральное число N, а затем N чисел.
# По данным числам, определите количество чисел, которые равны нулю
def count_numbers_equel_zero() -> int:
    numbers = int(input())

    count_zero = 0

    for _ in range(numbers):
        if int(input()) == 0:
            count_zero += 1

    return count_zero

# Задача 3*
# Вводится натуральное число N, а затем N чисел.
# Найти средее арифметическое всех чисел кратных 3. Если таких чисел нет, то вывести -1
def average_number_multiple_three() -> float:
    numbers = int(input())

    sum = 0
    total_num_multiple_three = 0

    for _ in range(numbers):
        target_num = int(input())

        if target_num % 3 == 0:
            sum += target_num
            total_num_multiple_three += 1

        if not total_num_multiple_three:
            return -1

    return sum / total_num_multiple_three