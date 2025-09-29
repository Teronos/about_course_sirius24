package main

import (
	"fmt"
	"math"
)

func main() {

	var num int
	multi_num := 1

	fmt.Print("Введите пятизначное число: ")
	fmt.Scan(&num)

	if int(math.Log10(float64(num)))+1 == 5 {

		for i := 1; i < 5; i++ {
			multi_num *= num % 10
			num = num / 10
		}

		fmt.Print(multi_num)

	} else {
		fmt.Print("Введите пятизначное число!")
	}
}
