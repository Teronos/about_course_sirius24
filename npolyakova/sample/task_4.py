# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что 𝜑𝑛=𝐴 .
# Если А не является числом Фибоначчи, выведите число -1.

numberA = int(input("Введите натуральное число больше 1: "))

if numberA <= 1 or numberA == "":
    print("Ошибка ввода данных")
    exit(0)

try:
    int(numberA)
except ValueError:
    print("Ошибка ввода данных")
    exit(0)

if numberA == 0:
    print(0)
elif numberA == 1:
    print(1)
else:
    fib1 = 0
    fib2 = 1
    fibN = 0
    count = 2
    while fibN <= numberA:
        if fib1 + fib2 == numberA:
            print(count)
            break
        if fib1 + fib2 > numberA:
            print(-1)
            break
        fibN = fib1 + fib2
        fib1 = fib2
        fib2 = fibN
        count = count + 1
