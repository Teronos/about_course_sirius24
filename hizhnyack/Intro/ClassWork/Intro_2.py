#Дано трехзначное число. Переверните его, а затем выведите.
#
#Пример ввода:
#
#843
#
#Пример вывода:
#
#348
print("Дано трехзначное число. Переверните его, а затем выведите")
a=input("Введите 3х-значное число: ")
if a.isnumeric():
    if len(a)!=3:
        print ("Введено НЕ трёхзначное число!")
    else:
        print("Перевёрнутое число: ",int(a[::-1]))
else:
    print("Введено НЕ число!")
