# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.
# Пример ввода:
# 1
# 3
# 3
# 1
# 0
# Пример вывода:
# 2
list_n = list()
count = 0
maxes_count = 1
print('Введите несколько натуральных чисел.\nДля завершения ввода введите 0 ')
list_n.append(int(input(f'Введите {count + 1}-е число последовательности: ')))
max_in_list = list_n[0]
while list_n[count] != 0:
    count += 1
    list_n.append(int(input(f'Введите {count + 1}-е число последовательности: ')))
    if list_n[count] == max_in_list:
        maxes_count += 1
    if list_n[count] > max_in_list:
        max_in_list = list_n[count]
        maxes_count = 1
print(f'Максимальное число в последовательности - {max_in_list}. Последовательность содержит {maxes_count} таких чисел')
if input('Вывести последовательность для проверки результата (y/n)?  ') == "y":
    print (list_n)
