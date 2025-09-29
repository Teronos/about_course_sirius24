# По данному числу N распечатайте все целые значения степени двойки, не превосходящие N, в порядке возрастания.

N = int(input())
power = 1

while True:
    power *= 2
    if power > N:
        break
    print(power, end=' ')
