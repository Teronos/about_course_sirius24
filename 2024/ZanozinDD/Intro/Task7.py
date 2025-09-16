#Задание 7
n = int(input("Введите количество чисел: "))
seq = list(map(int, input("Введите числа через пробел: ").split()))
sum_of_numbers = 0

for number in seq:
    if 10 <= number <= 99 and number % 8 == 0:
        sum_of_numbers += number

print("Сумма двузначных чисел, кратных 8:", sum_of_numbers)

#Задание 7*
N = int(input("Введите количество чисел: "))
numbers = []
i = 0

for _ in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

m_num = max(numbers)
i = numbers.count(m_num)

print(i)