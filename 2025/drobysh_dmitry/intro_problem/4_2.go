package main

import (
    "fmt"
)

func checkFibo(n int) int{
	if(n == 0){
		return 0
	} else if(n == 1){
		return 1
	}

	index := 2
	prev := 1
	current := 1
	tmp := 0
	for current < n{
		index++
		tmp = current
		current+=prev
		prev = tmp
	}

	if current == n{
		return index
	} 

	return -1
}

func main(){
    var num int = 0
    _, err := fmt.Scan(&num)

    if err!=nil{
        fmt.Println("Error while input function :", err)
        return
    }
    fmt.Println(checkFibo(num))
}
