# Задание 2
def reverse_number(n):
    return int(str(n)[::-1])

input_number = 843
output = reverse_number(input_number)
print(output)  # Вывод: 348


# Задание 2*
def sum_even_odd_digits(n):
    even_sum = 0
    odd_sum = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return int(str(even_sum) + str(odd_sum))

input_number = 531893
output = sum_even_odd_digits(input_number)
print(output)  # Вывод: 821
