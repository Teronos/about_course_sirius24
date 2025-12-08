package main

import "fmt"

func main() {
	var num int
	var multi = 1
	fmt.Print("Введите число: ")
	fmt.Scan(&num)
	if num == 0 {
		multi = 0
	}
	for num > 0 {
		multi *= num % 10
		num /= 10
	}
	fmt.Println(multi)
}
