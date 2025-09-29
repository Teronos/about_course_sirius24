N = int(input())
numbers = [int(input()) for _ in range(N)]

multiples_of_3 = [x for x in numbers if x % 3 == 0] 

if multiples_of_3:
    avg = sum(multiples_of_3) / len(multiples_of_3)
    print(avg)
else:
    print(-1)
