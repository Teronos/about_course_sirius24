package main

import (
    "fmt"
    util "main/util"
)

func main(){
    var solver util.CaseSolver
    var num int = 0

    mul := 1
    _, err := fmt.Scan(&num) 
    
    if err!=nil{
        fmt.Println("Error while input function :", err)
        return
    }

    checkLength, message := solver.ValidateLengthInteger(num, 5)
    fmt.Println(num)
    if(!checkLength){
        fmt.Println("Error :", message)
        return
    }

    for num > 0{
        mul *= num%10
        num/=10
    }

    fmt.Println(mul)
}

