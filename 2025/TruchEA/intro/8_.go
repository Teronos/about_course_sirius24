package main

import "fmt"

func create_matrix(size int) [][]int {

	matrix := make([][]int, size)

	for i := range matrix {
		matrix[i] = make([]int, size)
	}

	for i := 0; i < size; i++ {

		fmt.Printf("Введите %d чисел для строки %d через пробел: ", size, i+1)

		for j := 0; j < size; j++ {
			fmt.Scan(&matrix[i][j])
		}
	}

	//fmt.Println("Введённая квадратная матрица:")
	return matrix
}

func my_sort(matrix [][]int) []int {
	var snail []int

	if len(matrix) == 0 {
		return snail
	}

	top, bottom := 0, len(matrix)-1
	left, right := 0, len(matrix[0])-1

	for top <= bottom && left <= right {
		// ➡ идём слева направо по верхней строке
		for j := left; j <= right; j++ {
			snail = append(snail, matrix[top][j])
		}
		top++

		// ⬇ идём сверху вниз по правому столбцу
		for i := top; i <= bottom; i++ {
			snail = append(snail, matrix[i][right])
		}
		right--

		// ⬅ идём справа налево по нижней строке
		if top <= bottom {
			for j := right; j >= left; j-- {
				snail = append(snail, matrix[bottom][j])
			}
			bottom--
		}

		// ⬆ идём снизу вверх по левому столбцу
		if left <= right {
			for i := bottom; i >= top; i-- {
				snail = append(snail, matrix[i][left])
			}
			left++
		}
	}

	return snail
}

func main() {

	var size_matrix int

	fmt.Print("Введите размерность матрицы: ")
	_, err_1 := fmt.Scanf("%d\n", &size_matrix)

	if size_matrix < 0 {
		fmt.Println("Ошибка: размерность должна быть положительным числом")
		return
	}
	if err_1 != nil {
		fmt.Println("Ошибка: введите целое число")
		return
	}

	matrix := create_matrix(size_matrix)

	fmt.Println("Матрица:")
	fmt.Print(matrix)

	fmt.Println("\nПолученная улитка:")
	fmt.Print(my_sort(matrix))
}
