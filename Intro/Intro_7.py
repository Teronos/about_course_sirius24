# Задача 7
# Напишите программу, которая в последовательности чисел
# находит сумму двузначных чисел, кратных 8.
# Программа в первой строке получает на вход число n -
# количество чисел в последовательности, во второй строке --
# n чисел, входящих в данную последовательность.
# Пример ввода:
# 5
# 38 24 800 8 16
# Пример вывода:
# 40
import random

list_n = list()
summ = 0
n = int(input("Укажите длину последовательности: "))
if input("По умолчанию последовательность будет сгенерирована автоматически.\nХотите ввести числа вручную(y/n)? ") == "y":
    for count in range(0,n):
        list_n.append(int(input(f"Введите {count+1}-е число последовательности: ")))
else:
    for count in range(0,n):
        list_n.append(int(random.uniform(-1,1)*1000))
for count in range(0, n):
    if list_n[count]%8 == 0 and ((len(str(list_n[count])) == 2 and (list_n[count] > 0)) or (len(str(list_n[count])) == 3 and list_n[count] < 0)):
        summ += list_n[count]
print(f"Сумма двузначных чисел, кратных 8 составляет: ",summ)
if input("Вывести последовательность для проверки результата (y/n)?  ") == "y":
    print (list_n)
if input("Вывести двузначные числа, кратные 8 (y/n)?  ") == "y":
    for count in range(0, n):
            if list_n[count]%8 == 0 and (len(str(list_n[count])) == 2 and (list_n[count] > 0)) or (len(str(list_n[count])) == 3 and list_n[count] < 0):
                print(list_n[count])
