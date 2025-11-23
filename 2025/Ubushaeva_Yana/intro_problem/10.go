package main

import (
	"fmt"
)

type Promise struct {
	Id     int
	Salary float64
	Paid   bool
}

type Employee struct {
	FirstName  string
	SecondName string
	Id         int
	Promise    *Promise
}

type Director struct {
	Employee
	company *Company
}

func (d *Director) CheckPromises() bool {
	for _, emp := range d.company.Employees {
		if !emp.Promise.Paid {
			return false
		}
	}
	if d.company.Director != nil && !d.company.Director.Promise.Paid {
		return false
	}
	return true
}

type Company struct {
	Balance   float64
	Director  *Director
	Employees []*Employee
}

func NewCompany(balance float64) *Company {
	return &Company{Balance: balance}
}

func (c *Company) CreateDirector(firstName, secondName string, id int, salary float64) {
	d := &Director{
		Employee: Employee{
			FirstName:  firstName,
			SecondName: secondName,
			Id:         id,
			Promise: &Promise{
				Id:     id,
				Salary: salary,
				Paid:   false,
			},
		},
		company: c,
	}
	c.Director = d
}

func (c *Company) CreateEmployee(firstName, secondName string, id int, salary float64) {
	e := &Employee{
		FirstName:  firstName,
		SecondName: secondName,
		Id:         id,
		Promise: &Promise{
			Id:     id,
			Salary: salary,
			Paid:   false,
		},
	}
	c.Employees = append(c.Employees, e)
}

func (c *Company) SetProfit(profit float64) {
	c.Balance += profit
}

func (c *Company) FulfillPromise() bool {
	total := 0.0
	if c.Director != nil {
		total += c.Director.Promise.Salary
	}
	for _, emp := range c.Employees {
		total += emp.Promise.Salary
	}

	if c.Balance < total {
		if c.Director != nil {
			c.Director.Promise.Paid = false
		}
		for _, emp := range c.Employees {
			emp.Promise.Paid = false
		}
		return false
	}

	c.Balance -= total
	if c.Director != nil {
		c.Director.Promise.Paid = true
	}
	for _, emp := range c.Employees {
		emp.Promise.Paid = true
	}
	return true
}

func main() {
	vk := NewCompany(50)

	vk.CreateDirector("Владимир", "Кириенко", 1, 15)
	vk.CreateEmployee("Елена", "Иванова", 2, 8)
	vk.CreateEmployee("Виктор", "Кузнецов", 3, 6)

	vk.SetProfit(145.12)
	fmt.Println(vk.FulfillPromise())

	director := vk.Director
	fmt.Println(director.CheckPromises())

	vk.SetProfit(-200)
	fmt.Println(vk.FulfillPromise())
	fmt.Println(director.CheckPromises())
}
