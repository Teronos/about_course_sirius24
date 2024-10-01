# array = [ [1,2,3], [4,5,6], [7,8,9] ]
array = [ [1,2,3,1], [4,5,6,4], [7,8,9,7], [7,8,9,7]]


def funk (matrix):
    result = []
    while matrix:
        
        # верхняя строка
        result += matrix.pop(0)

        # print(f"matrix {matrix}")
        # print(f"result {result}")
        # print("\n")

        if matrix and matrix[0]:
            # последний элемент каждого оставшегося ряда (справа налево)
            for row in matrix:
                result.append(row.pop())
        
        if matrix:
            # последнюю строку в обратном порядке
            result += matrix.pop()[::-1]
        
        if matrix and matrix[0]:
            # первый элемент каждого оставшегося ряда (слева направо)
            for row in matrix[::-1]:
                result.append(row.pop(0))
    
    return result









if __name__ == "__main__":
    print(funk(array))