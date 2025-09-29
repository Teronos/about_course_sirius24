package main

import "fmt"

func max_el_list(lst_num []int) int {
	max_num := lst_num[0]
	for _, element := range lst_num[1:] {
		max_num = max(max_num, element)
	}

	return max_num
}

func main() {

	var num int
	var chek_num int
	var lst_num []int

	fmt.Print("Введите количество проверяемых цифр: ")
	_, err_1 := fmt.Scanf("%d\n", &num)

	if num < 0 {
		fmt.Println("Ошибка: количество должно быть положительным числом")
		return
	}
	if err_1 != nil {
		fmt.Println("Ошибка: введено не число")
		return
	}

	for i := 0; i < num; i++ {

		fmt.Print("Введите целое число: ")
		_, err_2 := fmt.Scanf("%d\n", &chek_num)

		if err_2 != nil {
			fmt.Println("Ошибка: введите целое число")
			return
		}

		lst_num = append(lst_num, chek_num)
	}

	/*
		max_num := lst_num[0]
		for _, element := range lst_num[1:] {
			max_num = max(max_num, element)
		}*/

	fmt.Println("Максимальное число:", max_el_list(lst_num))
}
