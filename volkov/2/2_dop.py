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
sum_nechet = 0
sum_chet = 0
var = False
while x > 0:
    if var : 
        sum_nechet += x % 10  # Добавляем последнюю цифру к сумме
        var = False
    else: 
        sum_chet += x % 10  # Добавляем последнюю цифру к сумме
        var = True
    x //= 10  # Убираем последнюю цифру


print(sum_nechet, end="")
print(sum_chet, end="")

print("\n")
