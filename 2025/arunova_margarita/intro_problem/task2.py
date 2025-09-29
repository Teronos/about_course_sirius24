"""
Дано шестизначное число. Найдите суммы его четных и нечетных элементов.
Образуйте из них этих сумм одно числ и выведите его на экран.

Пример ввода:
531893

Пример вывода:
1514
"""

num, sum_even, sum_odd = input("Введите шестизначное число: "), 0, 0
for i in range(len(num)):
    digit = int(num[i])
    if i % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
print("Итоговое число:",  str(sum_even) + str(sum_odd))
