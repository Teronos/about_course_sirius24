# Дано пятизначное число. Найдите произведение его цифр

number = input().strip()
product = 1

for digit in number:
    product *= int(digit)

print(product)