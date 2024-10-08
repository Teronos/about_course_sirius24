# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.

numList = []
count = 0

print("Введите последовательность чисел, где 0 будет последним числом:  ")
number = input()

if number == "":
    print("Ошибка ввода данных")
    exit(0)

while number != "0":
    try:
        int(number)
    except ValueError:
        print("Ошибка ввода данных")
        exit(0)
    numList.append(int(number))
    number = input()

if number == "0":
    numList.append(int(number))

maximum = max(numList)

for item in numList:
    if item == maximum:
        count += 1

print(count)
