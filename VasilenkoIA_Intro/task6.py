#Задача 6*
#Сначала на вход поступает длина последовательности N. Затем элементы последовательности – целые числа. Напишите программу, которая подсчитывает количество положительных чисел среди элементов последовательности.

N = int(input("Введите длину последовательности: "))
sequence = []
for _ in range(N):
    num = int(input())
    sequence.append(num)
positive_count = 0
for num in sequence:
    if num > 0:
        positive_count += 1
print("Количество положительных чисел:", positive_count)