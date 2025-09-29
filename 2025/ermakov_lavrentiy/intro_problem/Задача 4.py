A = int(input())

f1, f2 = 0, 1
n = 0

while f1 < A:
    f1, f2 = f2, f1 + f2
    n += 1

if f1 == A:
    print(n)
else:
    print(-1)
8