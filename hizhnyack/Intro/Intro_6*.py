# Задача 6*
# Сначала на вход поступает длина последовательности N.
# Затем элементы последовательности – целые числа.
# Напишите программу, которая подсчитывает количество положительных
# чисел среди элементов последовательности.
# Пример ввода:
# 5
# 1
# 2
# 3
# -1
# -4
# Пример вывода:
# 3
import random

N = int(input("Укажите длину последовательности для генерации: "))
listN = list()
plus = 0
for count in range(0,N):
    listN.append(int(random.uniform(-1,1)*10))
    if listN[count] > 0:
        plus +=1
print(f"Количество положительных чисел в последовательности: ",plus)
if input("Вывести последовательность для проверки результата (y/n)?  ") == "y":
    print (listN)
