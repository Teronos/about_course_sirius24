package main

import "fmt"

func fibonacciIndexRec(inp_num, f_1, f_2, index int) int {

	if f_2 > inp_num {
		return -1
	}

	if f_2 == inp_num {
		return index
	}

	return fibonacciIndexRec(inp_num, f_2, f_1+f_2, index+1)
}

func main() {

	var inp_num int

	fmt.Print("Введите целое число: ")
	inp_num_, err := fmt.Scan(&inp_num)

	if err != nil || inp_num_ != 1 {
		fmt.Println("Ошибка, введено не натуральное число")
		return
	}

	if inp_num <= 1 {
		fmt.Println(-1)
		return
	}

	fmt.Println(fibonacciIndexRec(inp_num, 1, 1, 2))
}
