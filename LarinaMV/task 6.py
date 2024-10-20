# На ввод подаются N целых чисел, их нужно сохранить в массив или список. 
# Затем вывести макимальный элемент

N= input()
Spisok =[]
max = int(N[0])
for _ in range(int(N)):
  i=int(input())
  Spisok.append(i)
  if i>max:
    max=i

print (max)
