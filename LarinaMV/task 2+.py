#Дано шестизначное число. Найдите суммы его четных и нечетных элементов. 
#Образуйте из них этих сумм оддно числ ои выведите его на экран
n= input("Введите шестизначное число: ")
sum1=0
sum2=0
for i in range(0,6):
  if int(i)%2 ==0:
    sum1=sum1+int(n[i])
  else:
    sum2=sum2+int(n[i])
print("Ответ: ", str(sum1)+str(sum2))