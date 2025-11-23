# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

print(numbers.count(max(numbers)))