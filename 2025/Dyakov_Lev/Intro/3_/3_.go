package main

import "fmt"

func main() {
	var (
		num   int
		digit int     = 0
		count float32 = 0.
		sum   float32 = 0.
	)
	fmt.Print("Количество чисел: ")
	fmt.Scan(&num)
	for i := 0; i < num; i++ {
		fmt.Scan(&digit)
		if digit%3 == 0 {
			count++
			sum += float32(digit)
		}
	}
	/**/
	if sum == 0 {
		fmt.Print(-1)
	} else {
		fmt.Print(sum / count)
	}
}
