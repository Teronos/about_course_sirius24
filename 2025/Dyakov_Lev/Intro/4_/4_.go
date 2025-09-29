package main

import "fmt"

func main() {
	var a int
	fmt.Print("Введите число: ")
	fmt.Scan(&a)
	fmt.Print(fib_search(a))
}

func fib_search(a int) int {
	if a <= 0 {
		return -1
	}
	x, y := 0, 1
	n := 1
	for y < a {
		x, y = y, x+y
		n++
	}
	if y == a {
		return n
	}
	return -1
}
