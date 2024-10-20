#Вводится натуральное число N, а затем N целых чисел последовательности.
#Найдите количество минимальных элементов в последовательности

N= input("Введите натуральное число N:")
Spisok =[]
count = 0
for _ in range(int(N)):
  i=int(input())
  Spisok.append(i)

min = Spisok[0]

for i in Spisok:
  if i<min:
    min=i

for i in Spisok:
  if i==min:
    count+=1
print (count)