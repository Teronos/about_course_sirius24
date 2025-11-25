#Вводится натуральное число N, а затем N целых чисел последовательности. Найдите количество минимальных элементов в последовательности.
#Пример ввода:
#3
#21
#11
#4
#Пример вывода:
#1

n = int(input())
min_value = None
count = 0
for i in range(n):
    num = int(input())
    if min_value is None or num < min_value:
        min_value = num
        count = 1
    elif num == min_value:
        count += 1
print(count)