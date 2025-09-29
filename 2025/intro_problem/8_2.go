package main

import (
    "fmt"
)

func convert(arr [][]int) []int{
    N := len(arr)
    ans := make([]int, 0, N*N)
    shift := 0

    for shift <= N-1 {
        // upper line
        for i := shift; i < N; i++{
            ans = append(ans, arr[shift][i])
        }


        // right line
        for i := shift + 1; i < N - 1; i++{
            ans = append(ans, arr[i][N-1])
        }

        // bottom line
        for i := N - 1; i >= shift; i--{
            ans = append(ans, arr[N-1][i])
        }


        // left line
        for i := N - 2; i > shift; i--{
            ans = append(ans, arr[i][shift])
        }

        shift++
        N--
    }

    if len(arr)%2 != 0{
        return ans[0:len(arr)*len(arr)] 
    }

    return ans

}

func main(){
    twoDArr := [][]int{{1,2,3}, {4,5,6}, {7,8,9}}
    for i := 0; i < 3; i++{
        fmt.Println(twoDArr[i])
    }
    fmt.Println(convert(twoDArr))
    
    twoDArr2 := [][]int{{1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}}
    for i := 0; i < 4; i++{
        fmt.Println(twoDArr2[i])
    }

    fmt.Println(convert(twoDArr2))
}
