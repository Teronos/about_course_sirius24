# Задача 1
def sum_digits(n):
    return sum(int(digit) for digit in str(n))

input_number = 358
output = sum_digits(input_number)
print(output)  # Вывод: 16

# Задача 1*
def mlt_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

input_number = 14962
output = mlt_digits(input_number)
print(output)  # Вывод: 432
