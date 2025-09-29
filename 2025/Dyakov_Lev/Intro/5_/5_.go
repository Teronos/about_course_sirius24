package main

import (
	"fmt"
	"math"
)

func main() {
	var num float64
	fmt.Print("Введите число:")
	fmt.Scan(&num)
	for i := 0.; math.Pow(2, i) < num; i++ {
		fmt.Print(math.Pow(2, i), " ")
	}
}
