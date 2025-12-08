package main

import "fmt"

func main() {
	array := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16},
	}

	res := my_sort(array)
	fmt.Println(res)
}

// array[i][j]
func my_sort(array [][]int) []int {
	n := len(array)
	result := make([]int, 0, n*n)
	top, bottom := 0, n-1
	left, right := 0, n-1
	for left <= right && top <= bottom {
		for i := left; i <= right; i++ {
			result = append(result, array[top][i])
		}
		top++

		for i := top; i <= bottom; i++ {
			result = append(result, array[i][right])
		}
		right--

		if top < bottom {
			for i := right; i >= left; i-- {
				result = append(result, array[bottom][i])
			}
			bottom--
		}

		if right > left {

			for i := bottom; i >= top; i-- {
				result = append(result, array[i][left])
			}
			left++
		}
	}
	return result
}
