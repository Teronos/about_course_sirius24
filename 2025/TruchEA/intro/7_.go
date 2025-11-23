package main

import "fmt"

func max_el_list(lst_num []int) int {

	max_num := lst_num[0]

	for _, element := range lst_num[1:] {
		max_num = max(max_num, element)
	}

	return max_num
}

func amount_equel_max_el(lst_num []int) int {

	amount := 0
	max_el := max_el_list(lst_num)

	for _, element := range lst_num {
		if element == max_el {
			amount += 1
		}
	}

	return amount
}

func main() {

	//var num int
	var chek_num int
	var lst_num []int
	stop_number := 0

	/*
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
	*/

	for i := 0; ; i++ {

		fmt.Print("Введите целое число: ")
		_, err_2 := fmt.Scanf("%d\n", &chek_num)

		if err_2 != nil || chek_num < 0 {
			fmt.Println("Ошибка: введите натуральное число")
			return
		}

		if chek_num != stop_number {
			lst_num = append(lst_num, chek_num)
		} else {
			lst_num = append(lst_num, chek_num)
			break
		}
	}

	fmt.Println(":", amount_equel_max_el(lst_num))
}
