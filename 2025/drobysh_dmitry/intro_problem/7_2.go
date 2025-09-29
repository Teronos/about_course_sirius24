package main

import (
    "fmt"
)

func main(){
    ans := 1
    maxi := 0
    _, err := fmt.Scan(&maxi)
    if err != nil{
        fmt.Println("Error while input function (On maxi element) :", err)
        return
    }

    tmp := maxi
    for tmp != 0{
        _, err = fmt.Scan(&tmp)
        if err != nil{
            fmt.Println("Error while input function (on elements) :", err)
            return
        }

        if tmp == maxi{
            ans++
        }

        if tmp > maxi{
            ans = 1
            maxi = tmp
        }
    }

    fmt.Println(ans)



    

}
