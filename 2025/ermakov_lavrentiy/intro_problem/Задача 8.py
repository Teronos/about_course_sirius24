def my_sort(arr):
    if not arr:
        return []
    
    N = len(arr)
    result = []
    shift = 0
    
    while shift <= N - 1 - shift:
        # Верхняя строка: слева направо
        for i in range(shift, N - shift):
            result.append(arr[shift][i])
        
        # Правый столбец: сверху вниз
        for i in range(shift + 1, N - 1 - shift):
            result.append(arr[i][N - 1 - shift])
        
        # Нижняя строка: справа налево (если есть)
        if shift != N - 1 - shift:
            for i in range(N - 1 - shift, shift - 1, -1):
                result.append(arr[N - 1 - shift][i])
        
        # Левый столбец: снизу вверх (если есть)
        if shift != N - 1 - shift:
            for i in range(N - 2 - shift, shift, -1):
                result.append(arr[i][shift])
        
        shift += 1
    
    return result

array1 = [[1,2,3], [4,5,6], [7,8,9]]
print("Матрица 3x3:")
for row in array1:
    print(row)
print("Результат:", my_sort(array1))  # [1,2,3,6,9,8,7,4,5]
print()

array2 = [[1,2,3], [8,9,4], [7,6,5]]
print("Матрица 3x3 (спираль):")
for row in array2:
    print(row)
print("Результат:", my_sort(array2))  # [1,2,3,4,5,6,7,8,9]
print()

array3 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print("Матрица 4x4:")
for row in array3:
    print(row)
print("Результат:", my_sort(array3))