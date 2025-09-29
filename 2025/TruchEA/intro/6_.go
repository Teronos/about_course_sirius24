package main

import "fmt"

func amount_positive(lst_nums []int) int {
	amount := 0

	for _, el := range lst_nums {
		if el > 0 {
			amount += 1
		}
	}
	//fmt.Println("Количество положительных чисел", amount)
	return amount
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
		fmt.Println("Ошибка: введено не целое число")
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

	fmt.Print(amount_positive(lst_num))
}
