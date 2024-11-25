i = 0
mas = []
bool_end = True
while bool_end:

    is_int = False

    while is_int == False:
        print(f"введите число №{i+1}: ", end="")
        try:
            inn = int(input())
            is_int = True
            
        except:
            print(f"введите челое число ")
    
    mas.append(inn)

    if inn == 0:
        bool_end = False

    i += 1

maxim = -9999999999999999
kol_max = 0
print(mas)

for i in mas:
    if i > maxim:
        maxim = i
        kol_max = 1
    elif i == maxim:
        kol_max +=1


print(kol_max)
