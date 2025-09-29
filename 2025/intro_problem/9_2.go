package main

import "fmt"

type Laptop struct{
    Brand string
    Model string
    Price int
}

func newLaptop(brand string, model string, price int) *Laptop{
    return &Laptop{
        Brand : brand, 
        Model:model, 
        Price:price,
    }
}

func main(){
    myLaptop := newLaptop("Dell", "G15", 57000)
    fmt.Println(myLaptop)

}
