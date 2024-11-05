# Задача 3
n = int(input("Введите число: "))
i = 0
for _ in range(n):
    number = int(input("Введите число: "))
    if number == 0:
        i += 1

print("Количество чисел, равных нулю =", i)


# Задача 3*
n = int(input("Введите количество чисел: "))
numbers = []
for _ in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

mlt_of_3 = [num for num in numbers if num % 3 == 0]

if mlt_of_3:
    average = sum(mlt_of_3) / len(mlt_of_3)
    print("Mod 3 =", average)
else:
    print(-1)