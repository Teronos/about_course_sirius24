
is_int = False

while is_int == False:
    try:
        a = int(input("Введите число a: "))
        is_int = True
    except:
        print(f"введите челое число")

is_int = False

while is_int == False:
    try:
        b = int(input("Введите число b: "))
        if b >= a:
            is_int = True
        else:
            is_int = False
    except:
        print(f"введите челое число b >=a")

is_int = False
for i in range(b, a, -1):
    # print(i)
    if 0 == (i % 7):
        print(i)
        is_int = True
        break

if is_int is False:
    print("-1")