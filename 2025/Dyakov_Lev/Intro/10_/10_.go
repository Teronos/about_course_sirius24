package main

import "fmt"

//ЗП
type Promise struct {
	id        int
	salary    float64
	fulfilled bool
}

//////////////////////////////////////////////
//Директор
type Director struct {
	first_name  string
	second_name string
	id          int
	promise     Promise
}

type DirectorInterface interface {
	check_promises() bool
}

//проверка выплаты ЗП
func (d *Director) check_promises() bool {
	return d.promise.fulfilled
}

//////////////////////////////////////////////

//////////////////////////////////////////////
//Работник
type Employee struct {
	first_name  string
	second_name string
	id          int
	promise     Promise
}

//////////////////////////////////////////////

//////////////////////////////////////////////
//Компания
type Company struct {
	balance   float64
	director  *Director
	employees []*Employee
}

type CompanyInterface interface {
	create_director(first_name, second_name string, id int, salary float64)
	create_employee(first_name, second_name string, id int, salary float64)
	set_profit(amount float64)
	get_director() *Director
	fulfill_promise() bool
}

// Создание директора
func (c *Company) create_director(first_name, second_name string, id int, salary float64) {
	c.director = &Director{
		first_name:  first_name,
		second_name: second_name,
		id:          id,
		promise:     Promise{id: id, salary: salary, fulfilled: false},
	}
}

// Создание работника
func (c *Company) create_employee(first_name, second_name string, id int, salary float64) {
	emp := &Employee{
		first_name:  first_name,
		second_name: second_name,
		id:          id,
		promise:     Promise{id: id, salary: salary, fulfilled: false},
	}
	c.employees = append(c.employees, emp)
}

// добавление выручки
func (c *Company) set_profit(amount float64) {
	c.balance += amount
}

// вытащить инфу о директоре
func (c *Company) get_director() *Director {
	return c.director
}

// Выплатить ЗП
func (c *Company) fulfill_promise() bool {
	totalSalaries := c.director.promise.salary
	for _, emp := range c.employees {
		totalSalaries += emp.promise.salary
	}

	if c.balance >= totalSalaries {
		c.balance -= totalSalaries

		c.director.promise.fulfilled = true
		for _, emp := range c.employees {
			emp.promise.fulfilled = true
		}
		return true
	} else {
		c.director.promise.fulfilled = false
		for _, emp := range c.employees {
			emp.promise.fulfilled = false
		}
		return false
	}
}

//////////////////////////////////////////////

func main() {
	vk := Company{balance: 50}

	vk.create_director("Владимир", "Кириенко", 1, 15)
	vk.create_employee("Елена", "Иванова", 2, 8)
	vk.create_employee("Виктор", "Кузнецов", 3, 6)

	vk.set_profit(145.12)
	ok := vk.fulfill_promise()
	fmt.Println("After profit 145.12, fulfill promise:", ok)
	fmt.Println("Director check promises:", vk.get_director().check_promises())

	vk.set_profit(-200)
	ok = vk.fulfill_promise()
	fmt.Println("After profit -200, fulfill promise:", ok)
	fmt.Println("Director check promises:", vk.get_director().check_promises())
}
