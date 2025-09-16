#Напишите функцию my_sort, которая принимает двумерный массив n x n, а возвращает элементы массива, 
#расположенные от самых крайних элементов до среднего элемента, таким образом, 
#чтобы происходило перемещение по часовой стрелке.
#То есть функция должна преобразовывать array = [ [1,2,3], [4,5,6], [7,8,9] ]
#my_sort(array) #=> [1,2,3,6,9,8,7,4,5]

def my_sort(matrix: list[list[int]]) -> list[int]:
    result = []
    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result

array = [ [1,2,3], [8,9,4], [7,6,5] ]
my_sort(array)