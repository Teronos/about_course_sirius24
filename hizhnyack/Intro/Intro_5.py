# По данному числу N распечатайте все целые значения степени двойки,
# не превосходящие N, в порядке возрастания.
# Пример ввода:
# 50
# Пример вывода:
# 1 2 4 8 16 32
N = int(input("Введите целое положительное число: "))
k = 0
print("Значения степени двойки, не превосходящие N, в порядке возрастания:")
while 2 ** k <= N:
    print (2 ** k)
    k += 1
