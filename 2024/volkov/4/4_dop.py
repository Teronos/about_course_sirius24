
is_int = False

while is_int == False:
    try:
        A = int(input("Введите число A (> 1): "))
        if A > 1:
            is_int = True
        else:
            is_int = False
    except:
        print(f"введите челое число больше 1")


fib1, fib2 = 0, 1
n = 1

while fib2 < A:
    fib1, fib2 = fib2, fib1 + fib2
    n += 1
    

if fib2 == A:
    print(n)
else:
    print(-1)