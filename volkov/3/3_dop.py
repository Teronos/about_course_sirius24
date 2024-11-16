print(f"введите кол-во чисел: ", end="")
is_int = False
sum_3 = 0
kol_3 = 0

while is_int == False:
    try:
        max_numder = int(input())
        is_int = True
    except:
        print(f"введите челое число ")



for i in range(0, max_numder):
    is_int = False

    while is_int == False:
        print(f"введите челое число №{i+1}: ", end="")
        try:
            inn = int(input())
            is_int = True
            
        except:
            print(f"введите челое число ")

    if (inn % 3) == 0:
        sum_3 += inn
        kol_3 +=1
        print(sum_3)

if sum_3 > 0:
    print(sum_3 / kol_3)
else:
    print("-1")