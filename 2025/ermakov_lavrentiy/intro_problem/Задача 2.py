num = input().strip()        # ожидаем шестизначное число как строку
odd_pos_sum = 0
even_pos_sum = 0

for i, ch in enumerate(num, start=1):   # индексы 1..6
    d = int(ch)
    if i % 2 == 1:
        odd_pos_sum += d
    else:
        even_pos_sum += d

print(f"{odd_pos_sum}{even_pos_sum}")
