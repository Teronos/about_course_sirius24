# По данному числу N распечатайте все целые значения степени двойки,
# не превосходящие N, в порядке возрастания

N= int(input("Введите натуральное число N:"))
stepen = 0
i=0
while True:
  i=2**stepen
  stepen = stepen +1
  if i>N:
    break
  print(i)
