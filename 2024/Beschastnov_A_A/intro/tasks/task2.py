#Задача 2.Дано трехзначное число. Переверните его, а затем выведите.
def my_reverse() -> int:
    numbers = input()

    return int(numbers[::-1])

#Задача 2*. Дано шестизначное число.
# Найдите суммы его четных и нечетных элементов. Образуйте из них этих сумм одно число и выведите его на экран
def sum_even_and_odd_nubmer() -> (int, int):
    numbers = input()

    result_even_sum = 0
    result_odd_sum = 0

    for index in range(len(numbers)):
        if index % 2 == 0:
            result_even_sum += int(numbers[index])
        result_odd_sum += int(numbers[index])

    return result_even_sum, result_odd_sum


