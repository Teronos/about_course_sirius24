# Вводится натуральное число N, а затем N целых чисел
# последовательности. Найдите количество
# минимальных элементов в последовательности.
# Пример ввода:
# 3
# 21
# 11
# 4
# Пример вывода:
# 1

print("Введите несколько натуральных чисел.\nДля завершения ввода нажмите ENTER либо введите не число/не натуральное число ")
k = 2
count = 1
smallest = input(f"Введите {k-1}-е число:  ")
N = input(f"Введите {k}-е число:  ")
while N.isnumeric():
    k += 1
    if N <= smallest:
        if smallest == N:
            count += 1
        smallest = N
    N = input(f"Введите {k}-е число:  ")
print(f"Самое маленькое число в последовательности:  ", smallest)
print(f"Количество самых маленьких чисел в последовательности:  ", count)
