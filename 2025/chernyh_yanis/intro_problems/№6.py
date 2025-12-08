'''
На ввод подаются N целых чисел, их нужно сохранить в массив или список. Затем вывести макимальный элемент.
Пример ввода:
5
2
3
56
45
21

Пример вывода:
56
'''


n = int(input())

massive_numbers = []


for i in range(n):
    num = int(input())
    massive_numbers.append(num)

max_number = max(massive_numbers)


print(max_number)