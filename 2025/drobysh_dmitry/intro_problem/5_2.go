package main

import (
    "fmt"
)

func main(){
    var num int = 0

    _, err := fmt.Scan(&num)

    if err!=nil{
        fmt.Println("Error while input function :", err)
        return
    }

    for i:=1; i <= num; i*=2{
        fmt.Printf("%d ", i)
    }

    fmt.Println()

}
