print(f"введите челое число ")
is_int = False

while is_int == False:
    try:
        x = int(input())
        is_int = True
    except:
        print(f"введите челое число ")


print(f"input {x}")

len = len(str(x))
print(f"len {len}")

print("\n")

sum_of_digits = 0


while x > 0:


    sum_of_digits += x % 10  # Добавляем последнюю цифру к сумме
    x //= 10  # Убираем последнюю цифру

    print("\n")

print(sum_of_digits)