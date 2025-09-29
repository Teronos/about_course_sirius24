package main

import "fmt"

func main() {
	var (
		max   int = -1
		digit int = -1
		count int = 0
	)
	for digit != 0 {
		fmt.Scan(&digit)
		if max < digit {
			max = digit
			count = 0
		}
		if max == digit {
			count++
		}
	}
	fmt.Print(count)
}
