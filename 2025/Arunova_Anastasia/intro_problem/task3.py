# Вводится натуральное число N, а затем N чисел. Найти среднее арифметическое всех чисел кратных 3.
# Если таких чисел нет, то вывести -1

N = int(input())
div_by_3_sum = 0
div_by_3_cnt = 0

for _ in range(N):
    num = int(input())
    if num % 3 == 0:
        div_by_3_sum += num
        div_by_3_cnt += 1

if div_by_3_cnt == 0:
    print(-1)
else:
    print(div_by_3_sum / div_by_3_cnt)