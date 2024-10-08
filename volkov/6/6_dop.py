print(f"введите кол-во чисел: ", end="")
is_int = False
kol_null = 0

while is_int == False:
    try:
        max_numder = int(input())
        is_int = True
    except:
        print(f"введите челое число ")

kol_pol = 0


for i in range(0, max_numder):
    is_int = False

    while is_int == False:
        print(f"введите число №{i+1}: ", end="")
        try:
            inn = int(input())
            is_int = True
            
        except:
            print(f"введите челое число ")

    if inn > 0:
        kol_pol += 1
        # print(f"min is {minimum}")
        # print(f"kol min {kol_min}")


    

print(kol_pol)