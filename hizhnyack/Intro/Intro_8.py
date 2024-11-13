# Задача 8*
# Напишите функцию my_sort, которая принимает двумерный массив n x n, а возвращает элементы массива,
# расположенные от самых крайних элементов до среднего элемента, таким образом,
# чтобы происходило перемещение по часовой стрелке.
# То есть функция должна преобразовывать array = [[1,2,3], [4,5,6], [7,8,9]]
# my_sort(array) #=> [1,2,3,6,9,8,7,4,5]
# Еще один пример работы функции:
# array = [[1,2,3], [8,9,4], [7,6,5] ] my_sort(array) #=> [1,2,3,4,5,6,7,8,9]
import random

def my_sort(array):
    sort = []
    j = n
    for k in range(0, j // 2):
        for i in range(k, j):
            sort.append(array[k][i])
        for i in range(k + 1, j):
            sort.append(array[i][j - 1])
        for i in range(j - 2, k - 1, -1):
            sort.append(array[j - 1][i])
        for i in range(j - 2, k, -1):
            sort.append(array[i][k])
        j -= 1
    if n % 2 > 0:
        sort.append(array[int(n / 2)][int(n / 2)])
    return sort

n = int(input('Введите размерность массива, n: '))
array = [[int(random.random()*10) for j in range(n)] for i in range(n)]
for i in range (0,n):
    print(array[i])

print(f'Массив, отсортированный по улитке: \n',my_sort(array))
