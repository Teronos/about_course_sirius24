package main

import "fmt"

func sum(nums []int) int {
	s := 0
	for _, n := range nums {
		s += n
	}
	return s
}

func avg(nums []int) float64 {

	if len(nums) == 0 {
		return -1
	}

	return float64(sum(nums)) / float64(len(nums))
}

func main() {

	var num int
	divisor := 3
	var chek_num int
	//average := 0
	var lst_num []int

	fmt.Print("Введите количество проверяемых цифр: ")
	fmt.Scan(&num)

	for i := 0; i < num; i++ {

		fmt.Print("Введите целое число: ")
		fmt.Scan(&chek_num)

		if chek_num%divisor == 0 {
			lst_num = append(lst_num, chek_num)
		}
	}

	fmt.Println("Среднее:", avg(lst_num))
}
