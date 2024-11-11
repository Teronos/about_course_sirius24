print(f"введите кол-во чисел: ", end="")
is_int = False
kol_null = 0

while is_int == False:
    try:
        max_numder = int(input())
        is_int = True
    except:
        print(f"введите челое число ")

# mas = []

for i in range(0, max_numder):
    is_int = False

    while is_int == False:
        print(f"введите челое число №{i+1}: ", end="")
        try:
            # mas.append(int(input()))
            inn = int(input())
            is_int = True
            
        except:
            print(f"введите челое число ")

    if inn == 0:
        kol_null += 1
        # print(kol_null)

print(kol_null)