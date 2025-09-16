#Задача 7*
#Последовательность состоит из натуральных чисел и завершается числом 0. Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

max_element = None
sequence = []
while True:
    num = int(input())
    if num == 0:
        break
    sequence.append(num)

    if max_element is None or num > max_element:
        max_element = num

count_max = 0
for num in sequence:
    if num == max_element:
        count_max += 1

print("Количество элементов, равных наибольшему элементу:", count_max)