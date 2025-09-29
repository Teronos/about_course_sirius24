package main

import "fmt"

func main(){
    sum := 0 
    amount := 0
    tmp := 0
    var n int = 0
    _, err := fmt.Scan(&n)
    if err != nil{
        fmt.Println("Error in input: ", err)
    }

    for i := 0; i < n; i++{
        _, err := fmt.Scan(&tmp)
        if err != nil{
            fmt.Println("Error in input: ", err)
        }

        if tmp % 3 == 0{
            amount++
            sum+=tmp
        }
    }


    if sum == 0 {
        sum = -1
        amount = 1
    }

    fmt.Println(float64(sum) / float64(amount))

}
