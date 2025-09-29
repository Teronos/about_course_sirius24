package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {

	var num int
	sum_even := 0 //сумма четных
	sum_odd := 0  //сумма нечетных

	fmt.Print("Введите шестизначное число: ")
	fmt.Scan(&num)

	if int(math.Log10(float64(num)))+1 == 6 {

		for i := 0; i < 6; i++ {

			if num%10%2 == 0 {
				sum_even += num % 10
			} else {
				sum_odd += num % 10
			}

			num = num / 10
		}

		fmt.Print(strconv.Itoa(sum_odd) + strconv.Itoa(sum_even))

	} else {
		fmt.Print("Введите шесизначное число!")
	}
}
