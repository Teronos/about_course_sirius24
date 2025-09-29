#Дано пятизначное число. Найдите произведение его цифр.
#Пример ввода:
#14962
#Пример вывода:
#432

number = input()
a, b, c, d, e = int(number[0]), int(number[1]), int(number[2]), int(number[3]), int(number[4])
print(a * b * c * d * e)