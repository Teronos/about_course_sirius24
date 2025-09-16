
is_int = False

while is_int == False:
    try:
        a = int(input("Введите число a: "))
        is_int = True
    except:
        print(f"введите челое число")


i = 0
while a > (2 ** i):
    print(f" {2 ** i}")
    i += 1