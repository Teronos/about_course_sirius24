import statistics

# Вводится натуральное число N, а затем N чисел.
# Найти средее арифметическое всех чисел кратных 3.
# Если таких чисел нет, то вывести -1

n = input("Введите кол-во чисел будущей последовательности N: ")
count = 0
numList = []

if n != "":
    try:
        int(n)
    except ValueError:
        print("Ошибка ввода данных")
        exit(0)

    for i in range(0, int(n)):
        el = input("Введите число " + str(i+1) + ": ")
        if int(el) % 3 == 0:
            numList.append(int(el))

    print(-1) if not numList else print(statistics.mean(numList))
else:
    print("Ошибка ввода данных, попробуйте ещё раз")
