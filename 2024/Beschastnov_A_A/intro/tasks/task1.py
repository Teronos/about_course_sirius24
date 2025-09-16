#Задача 1. Дано трехзначное число. Найдите сумму его цифр.
def sum_nubmer_sequences() -> int:
    numbers = input()

    result = 0

    for number in numbers:
        result += int(number)

    return result

#Задача 1*. Дано пятизначное число. Найдите произведение его цифр.
def mul_nubmer_sequences() -> int:
    numbers = input()

    result = 1

    for number in numbers:
        result *= int(number)

    return result