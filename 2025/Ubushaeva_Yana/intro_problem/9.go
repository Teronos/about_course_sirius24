package main

import (
	"fmt"
)

type Laptop struct {
	Brand string
	Model string
	Price int
}

func NewLaptop(brand, model string, price int) Laptop {
	return Laptop{
		Brand: brand,
		Model: model,
		Price: price,
	}
}

func (l Laptop) LaptopName() string {
	return l.Brand + " " + l.Model
}

func main() {
	hp := NewLaptop("hp", "15-bw0xx", 57000)

	fmt.Println(hp.Price)
	fmt.Println(hp.LaptopName())
}
