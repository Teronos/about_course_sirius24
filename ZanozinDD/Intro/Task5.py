#Задание 5
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

largest_of_7 = (b // 7) * 7

# Проверим, попадает ли это число в интервал [a, b]
if largest_of_7 >= a:
    print("Самое большое число, кратное 7 =", largest_of_7)
else:
    print(-1)

#Задание 5*
N = int(input("Введите число: "))
A = 1
while A <= N:
    print(A, end=',')
    A *= 2
print("\b")
