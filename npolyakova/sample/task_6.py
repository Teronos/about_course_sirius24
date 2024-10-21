# Сначала на вход поступает длина последовательности N. Затем элементы последовательности – целые числа.
# Напишите программу, которая подсчитывает количество положительных чисел среди элементов последовательности.

num = input("Введите число N: ")

if num == "":
    print("Ошибка ввода данных")
    exit(0)

try:
    int(num)
except ValueError:
    print("Ошибка ввода данных")
    exit(0)

if int(num) < 0:
    print("Кол-во чисел не может быть меньше 0")
    exit(0)

numList = [int(input()) for i in range(0, int(num))]
count = 0

for item in numList:
    if item > 0:
        count += 1

print(count)