# Дано шестизначное число. Найдите суммы его четных и нечетных элементов.
# Образуйте из них этих сумм одно число и выведите его на экран

number = input().strip()
even_sum = 0
odd_sum = 0

for i in range(0,6):
    if i % 2 == 0:
        even_sum += int(number[i])
    else:
        odd_sum += int(number[i])

print(str(even_sum) + str(odd_sum))