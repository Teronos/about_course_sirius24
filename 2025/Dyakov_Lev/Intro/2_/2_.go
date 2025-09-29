package main

import "fmt"

func main() {
	var even = 0
	var odd = 0
	var digit int
	var num int
	fmt.Print("Введите число: ")
	fmt.Scan(&num)
	for num > 0 {
		digit = num % 10
		if digit%2 == 0 {
			even += digit
		} else {
			odd += digit
		}
		num /= 10
	}
	fmt.Print(odd, "", even)
}
