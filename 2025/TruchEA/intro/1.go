package main

import (
	"fmt"
	"math"
)

func main() {

	var num int
	sum_num := 0

	fmt.Print("Введите трехзначное число: ")
	fmt.Scan(&num)

	if int(math.Log10(float64(num)))+1 == 3 {

		for i := 1; i < 4; i++ {
			sum_num += num % 10
			num = num / 10
		}

		fmt.Print(sum_num)
	} else {
		fmt.Print("Введите трехзначное число!")
	}
}
