#Задача 4*
#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn=A. Если А не является числом Фибоначчи, выведите число -1.

A = int(input())
fib_pred, fib_next = 0, 1
n = 1
while fib_next <= A:
  if fib_next == A:
    print(n)
    break
  fib_pred, fib_next = fib_next, fib_pred + fib_next
  n+=1
else:
  print(-1)