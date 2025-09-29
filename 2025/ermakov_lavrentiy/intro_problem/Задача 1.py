n = int(input())
product = 1
for digit in str(n):
    product *= int(digit)

print(product)