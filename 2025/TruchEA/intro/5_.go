package main

import (
	"fmt"
)

func main() {

	var num int
	var num_power []int
	power := 2

	fmt.Print("Введите число: ")
	_, err := fmt.Scan(&num)

	if err != nil {
		fmt.Println("Ошибка, введите число")
		return
	}

	i := 1

	for i <= num {
		num_power = append(num_power, i)
		i *= power
	}

	fmt.Println(num_power)
}
