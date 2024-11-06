#Задача 6
N = int(input("Введите количество чисел: "))
numbers = []

for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

print("Max =", max(numbers))

#Задача 6*
N = int(input("Введите количество чисел: "))
i = 0

for _ in range(N):
    number = int(input("Введите число: "))
    if number > 0: i += 1
print(i)
