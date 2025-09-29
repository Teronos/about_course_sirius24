max_num = 0
count_max = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n > max_num:
        max_num = n
        count_max = 1
    elif n == max_num:
        count_max += 1

print(count_max)
