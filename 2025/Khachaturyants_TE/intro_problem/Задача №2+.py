#Дано шестизначное число. Найдите суммы его четных и нечетных элементов. Образуйте из них этих сумм одно число и выведите его на экран
#Пример ввода:
#531893
#Пример вывода:
#1514

number = input()
even_sum = sum(int(d) for d in number if int(d) % 2 == 0)
odd_sum = sum(int(d) for d in number if int(d) % 2 != 0)
print(str(even_sum) + str(odd_sum))