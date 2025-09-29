package main

import (
    "fmt"
    util "main/util"
)

func superSum(num int, div int, size int) int{
    ans := 0
    for i := 0; i < size; i++{
        if i%2 == div{
            ans += num%10
        }
        num /= 10
    }

    return ans
}

func main(){
    var number int
    var solver util.CaseSolver
    _, err := fmt.Scan(&number)
    
    if err != nil{
        fmt.Println("Error while input function :", err)
        return
    }

    checkNumber, message := solver.ValidateLengthInteger(number, 6)
    
    if(!checkNumber){
        fmt.Println("Error :", message)
        return
    }


    fmt.Printf("%d%d\n", superSum(number, 1, 6), superSum(number, 0, 6))
}


















