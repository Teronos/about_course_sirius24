
_ = input()
list_num = list(map(int, input("Введите последовательность чисел: ").split()))
len = len(list_num)
sum = 0
for i in list_num:
    if (i < 100) and (i>9) and (0 == i % 8):
        sum += i

print(sum)