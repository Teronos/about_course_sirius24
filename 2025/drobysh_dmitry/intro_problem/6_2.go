package main

import (
    "fmt"
)

func main(){
    var ans int = 0
    var N int = 0
    _, err := fmt.Scan(&N)
    if err != nil{
        fmt.Println("Error while input function (On N element) :", err)
        return
    }

    tmp := 0

    for i := 0; i < N; i++{
        _, err = fmt.Scan(&tmp)
        if err != nil{
            fmt.Println("Error while input function (on elements) :", err)
            return
        }

        if tmp > 0{
            ans++
        }
    }

    fmt.Println(ans)



    

}
