package main

import "fmt"

type Laptop struct {
	brand string
	model string
	price int
}

type LaptopInterface interface {
	new(brand, model string, price int) *Laptop
	laptop_name() string
}

func new(brand, model string, price int) *Laptop {
	return &Laptop{
		brand: brand,
		model: model,
		price: price,
	}
}

func (l *Laptop) laptop_name() string {
	return l.brand + " " + l.model
}

func main() {
	hp := new("hp", "15-bw0xx", 57000)
	fmt.Println(hp.price)
	fmt.Print(hp.laptop_name())
}
