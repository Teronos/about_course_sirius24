#Задача 8
numb1 = input("Введите первое число: ")
numb2 = input("Введите второе число: ")

# Преобразование чисел в множества цифр
dig1 = set(numb1)
dig2 = set(numb2)
common_dig = dig1.intersection(dig2)
# Фильтрация и сохранение порядка из первого числа
result = [digit for digit in numb1 if digit in common_dig]
print("Цифры, входящие в запись обоих чисел:", ' '.join(result))

#Задача 8*
def my_sort(array):
    if not array or not array[0]:
        return []

    result = []
    n = len(array)
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        # Сначала проходим по верхнему ряду
        for i in range(left, right + 1):
            result.append(array[top][i])
        top += 1

        # Затем по правому столбцу
        for i in range(top, bottom + 1):
            result.append(array[i][right])
        right -= 1

        # Если еще остались строки, проходим по нижнему ряду
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(array[bottom][i])
            bottom -= 1

        # Если еще остались столбцы, проходим по левому столбцу
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(array[i][left])
            left += 1

    return result


array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_sort(array1))  # => [1, 2, 3, 6, 9, 8, 7, 4, 5]

