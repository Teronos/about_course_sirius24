package main

import "fmt"

//пусть это будет класс
type Laptop struct {
	brand string
	model string
	price float64
}
type LaptopInterface interface {
	new_laptop(brand, model string, price float64) *Laptop
	laptop_name() string
}

//допустим, это конструктор
func new_laptop(brand, model string, price float64) *Laptop {
	l := &Laptop{
		brand: brand,
		model: model,
		price: price,
	}
	return l
}

//о, вот это точно функция
func (l *Laptop) laptop_name() string {
	return (l.brand + " " + l.model)
}

func main() {
	var laptop Laptop = *new_laptop("hp", "15cpwk", 57000)
	fmt.Println(laptop.price)
	fmt.Println(laptop.laptop_name())
}
