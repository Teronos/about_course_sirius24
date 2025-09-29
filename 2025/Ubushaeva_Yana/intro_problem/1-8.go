package main

import (
	"fmt"
)

func findFibonacciIndex(A int) int {
	if A <= 1 {
		return -1
	}
	fib1, fib2 := 0, 1
	index := 1
	for fib2 < A {
		fib1, fib2 = fib2, fib1+fib2
		index++
	}
	if fib2 == A {
		return index
	}
	return -1
}

func complementaryDNK(dna string) string {
	complement := map[rune]rune{
		'A': 'T',
		'T': 'A',
		'C': 'G',
		'G': 'C',
	}

	var result []rune
	for _, nucleotide := range dna {
		if comp, exists := complement[nucleotide]; exists {
			result = append(result, comp)
		} else {
			return "Недопустимый символ."
		}
	}

	return string(result)
}

func mySort(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}

	n := len(matrix)
	res := []int{}

	top, bottom, left, right := 0, n-1, 0, n-1

	for top <= bottom && left <= right {
		for i := left; i <= right; i++ {
			res = append(res, matrix[top][i])
		}
		top++

		for i := top; i <= bottom; i++ {
			res = append(res, matrix[i][right])
		}
		right--

		if top <= bottom {
			for i := right; i >= left; i-- {
				res = append(res, matrix[bottom][i])
			}
			bottom--
		}

		if left <= right {
			for i := bottom; i >= top; i-- {
				res = append(res, matrix[i][left])
			}
			left++
		}
	}

	return res
}

func main() {

	var a string

	for {

		fmt.Println("Введите номер задачи (1, 1*, 2, 2*, 3, 3*, 4, 4*, 5, 5.1, 5*, 6, 6*, 7, 7*, 8, 8*):")
		var z string
		fmt.Scan(&z)
		switch z {

		case "1":
			fmt.Println("Задача 1. Дано трехзначное число. Найдите сумму его цифр.")
			var number_tree int
			fmt.Scan(&number_tree)
			if number_tree >= 100 && number_tree <= 999 {

				var sum_1 = number_tree/100 + number_tree/10%10 + number_tree%10
				fmt.Println(sum_1)

			} else {
				fmt.Println("Введено не трехзначное число")
			}

		case "1*":
			fmt.Println("Задача 1*. Дано пятизначное число. Найдите произведение его цифр.")
			var number_five int
			fmt.Scan(&number_five)
			if number_five >= 10000 && number_five <= 99999 {
				var sum_2 = (number_five / 10000) * (number_five / 1000 % 10) * (number_five / 100 % 10) * (number_five / 10 % 10) * (number_five % 10)
				fmt.Println(sum_2)

			} else {
				fmt.Println("Введено не пятизначное число")
			}

		case "2":
			fmt.Println("Задача 2. Дано трехзначное число. Переверните его, а затем выведите.")
			var number_tree2 int
			fmt.Scan(&number_tree2)
			if number_tree2 >= 100 && number_tree2 <= 999 {
				var rez = number_tree2/100 + number_tree2/10%10*10 + number_tree2%10*100
				fmt.Println(rez)
			} else {
				fmt.Println("Введено не трехзначное число")
			}

		case "2*":
			fmt.Println("Задача 2*. Дано шестизначное число. Найдите суммы его четных и нечетных элементов. ")
			fmt.Println("Образуйте из них этих сумм оддно числ ои выведите его на экран.")
			var number_six int
			fmt.Scan(&number_six)
			if number_six >= 100000 && number_six <= 999999 {
				var rez_chet = number_six/100000 + number_six/1000%10 + number_six/10%10
				var rez_nechet = number_six/10000%10 + number_six/100%10 + number_six%10
				fmt.Println(rez_chet, "", rez_nechet)
			} else {
				fmt.Println("Введено не шестизначное число")
			}

		case "3":
			fmt.Println("Задача 3. Вводится натуральное число N, а затем N чисел. По данным числам, определите количество чисел, которые равны нулю.")
			var n int
			fmt.Scan(&n)
			var count int
			for i := 0; i < n; i++ {
				var num int
				fmt.Scan(&num)
				if num == 0 {
					count++
				}
			}
			fmt.Println(count)

		case "3*":
			fmt.Println("Задача 3*. Вводится натуральное число N, а затем N чисел. Найти средее арифметическое всех чисел кратных 3. Если таких чисел нет, то вывести -1.")
			var n int
			fmt.Scan(&n)
			var count int
			count = 0
			var sum_3 int
			for i := 0; i < n; i++ {
				var num int
				fmt.Scan(&num)
				if num%3 == 0 {
					count++
					sum_3 += num
				}
			}
			if count != 0 {
				fmt.Println(float64(sum_3) / float64(count))
			} else {
				fmt.Println(-1)
			}

		case "4":
			fmt.Println("Задача 4. Вводится натуральное число N, а затем N целых чисел последовательности. Найдите количество минимальных элементов в последовательности.")
			var n int
			fmt.Scan(&n)

			if n <= 0 {
				fmt.Println("0")
				return
			}
			var x int
			fmt.Scan(&x)

			minVal := x
			count := 1

			for i := 1; i < n; i++ {
				fmt.Scan(&x)
				if x < minVal {
					minVal = x
					count = 1
				} else if x == minVal {
					count++
				}
			}
			fmt.Println(count)

		case "4*":
			fmt.Println("Задача 4*. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что . Если А не является числом Фибоначчи, выведите число -1.")
			var A int
			fmt.Print("Введите A > 1: ")
			fmt.Scan(&A)

			index := findFibonacciIndex(A)
			if index != -1 {
				fmt.Println(index)
			} else {
				fmt.Println(-1)
			}

		case "5":
			fmt.Println("Задача 5. Вводится два целых числа a и b (a <= b). Найдите самое большее число на отрезке от a до b, кратное 7. Если такого числа нет выведите -1.")
			var a, b int
			fmt.Println("Введите a и b, где a<=b: ")
			fmt.Scan(&a, &b)

			if a > b {
				fmt.Println("a>b")
				return
			}

			var largest_7 int = -1
			for i := b; i >= a; i-- {
				if i%7 == 0 {
					largest_7 = i
					break
				}
			}

			fmt.Println(largest_7)

		case "5.1":
			fmt.Println("Задача 5.1. В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и «G». Нужно написать программу, которая получате на вход последовательность ДНК и на выходе отображает комлементарную ей.")
			var dna string
			fmt.Scan(&dna)
			complementary := complementaryDNK(dna)
			fmt.Println(complementary)

		case "5*":
			fmt.Println("Задача 5*. По данному числу N распечатайте все целые значения степени двойки, не превосходящие N, в порядке возрастания.")
			var N int
			fmt.Scan(&N)
			if N < 1 {
				fmt.Println("N<1")
				return
			}
			powerOfTwo := 1
			for powerOfTwo <= N {
				fmt.Print(powerOfTwo, " ")
				powerOfTwo *= 2
			}

		case "6":
			fmt.Println("Задача 6. На ввод подаются N целых чисел, их нужно сохранить в массив или список. Затем вывести макимальный элемен.")
			var N int
			fmt.Scan(&N)
			if N <= 0 {
				fmt.Println("N<=0")
				return
			}
			numbers := make([]int, N)
			for i := 0; i < N; i++ {
				fmt.Scan(&numbers[i])
			}
			max := numbers[0]
			for _, number := range numbers[1:] {
				if number > max {
					max = number
				}
			}
			fmt.Println(max)
		case "6*":
			fmt.Println("Задача 6*. Сначала на вход поступает длина последовательности N. Затем элементы последовательности – целые числа. Напишите программу, которая подсчитывает количество положительных чисел среди элементов последовательности.")
			var N int
			fmt.Scan(&N)

			if N <= 0 {
				fmt.Println("N<=0")
				return
			}
			numbers := make([]int, N)
			for i := 0; i < N; i++ {
				fmt.Scan(&numbers[i])
			}
			count := 0
			for _, number := range numbers[0:] {
				if number > 0 {
					count++
				}
			}
			fmt.Println(count)

		case "7":
			fmt.Println("Задача 7. Напишите программу, которая в последовательности чисел находит сумму двузначных чисел, кратных 8. Программа в первой строке получает на вход число n - количество чисел в последовательности, во второй строке -- n чисел, входящих в данную последовательность.")
			var n int
			fmt.Scan(&n)
			var sum int
			for i := 0; i < n; i++ {
				var num int
				fmt.Scan(&num)
				if num >= 10 && num < 100 && num%8 == 0 {
					sum += num
				}
			}
			fmt.Println(sum)

		case "7*":
			fmt.Println("Задача 7*. Последовательность состоит из натуральных чисел и завершается числом 0. Определите количество элементов этой последовательности, которые равны ее наибольшему элементу.")
			var maxNum int
			var count int
			var num int
			maxNum = -1
			for {
				fmt.Scan(&num)
				if num == 0 {
					break
				}
				if num > maxNum {
					maxNum = num
					count = 1
				} else if num == maxNum {
					count++
				}
			}
			fmt.Println(count)

		case "8":
			fmt.Println("Задача 8. Даны два числа. Определить цифры, входящие в запись как первого, так и второго числа. Программа должна вывести цифры, которые имеются в обоих числах, через пробел. Цифры выводятся в порядке их нахождения в первом числе.")
			var a, b string
			fmt.Scan(&a, &b)

			digitsInB := make(map[rune]bool)
			for _, ch := range b {
				digitsInB[ch] = true
			}
			used := make(map[rune]bool)
			for _, ch := range a {
				if digitsInB[ch] && !used[ch] {
					fmt.Printf("%c ", ch)
					used[ch] = true
				}
			}

		case "8*":
			fmt.Println("Задача 8*. Напишите функцию my_sort, которая принимает двумерный массив n x n, а возвращает элементы массива, расположенные от самых крайних элементов до среднего элемента, таким образом, чтобы происходило перемещение по часовой стрелке.")
			array1 := [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			}
			fmt.Println(array1)
			fmt.Println(mySort(array1))
			fmt.Println()
			array2 := [][]int{
				{1, 2, 3, 1},
				{4, 5, 6, 4},
				{7, 8, 9, 7},
				{7, 8, 9, 7},
			}
			fmt.Println(array2)
			fmt.Println(mySort(array2))
		default:
			fmt.Println("Задачи нет. ")
		}

		fmt.Println("Продолжить?(Введите 0 чтобы закончить или любой символ для перехода к выбору задачи)")
		fmt.Scan(&a)
		if a == "0" {
			break
		}
	}
}
