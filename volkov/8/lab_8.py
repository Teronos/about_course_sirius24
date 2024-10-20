# Вводим два числа
num1, num2 = input("ыыедите 2 числа через пробел ").split()

digits_in_num2 = set(num2)

common_digits = []
for digit in num1:
    if digit in digits_in_num2 and digit not in common_digits:
        common_digits.append(digit)


print(" ".join(common_digits))
