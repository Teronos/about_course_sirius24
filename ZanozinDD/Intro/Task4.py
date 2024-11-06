#Задание 4
n = int(input("Введите количество чисел: "))
numbers = []
for _ in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)
    min_number=min(numbers)
    min_count = numbers.count(min_number)

print("Кол-во min чисел =", min_count)

#Задание 4*
fib1 = 1
fib2 = 1

A = int(input('Введите число: '))

n = 2
while fib2 < A:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    n += 1

if fib2 == A:print('Номер элемента в последовательности',n)
else: print(-1)
