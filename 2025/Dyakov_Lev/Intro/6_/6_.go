package main

import "fmt"

func main() {
	var (
		num   int
		digit int = 0
		count int = 0
	)
	fmt.Print("Введите число:")
	fmt.Scan(&num)
	for i := 0; i < num; i++ {
		fmt.Scan(&digit)
		if digit >= 0 {
			count++
		}
	}
	fmt.Print(count)
}
