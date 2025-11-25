#Дано трехзначное число. Найдите сумму его цифр.
#Пример ввода:
#745
#Пример вывода:
#16

number = input()
sum_of_digits = int(number[0]) + int(number[1]) + int(number[2])
print(sum_of_digits)