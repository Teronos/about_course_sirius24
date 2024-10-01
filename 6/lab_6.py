

list_num = list(map(int, input("Введите последовательность чисел: ").split()))
maximum = -99999999999
# i = 0
for i in list_num:
    if i > maximum:
        maximum = i

print(maximum)