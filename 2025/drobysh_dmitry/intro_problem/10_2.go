package main

import "fmt"

type ICompany interface{
    earn(flot int)
    payWage()
    printCompany()
}

type Promise struct{
    yearsLeft int
    wage int
}

type Director struct{
    firstName string
    lastName string
}

func newDirector(firstName string, lastName string) *Director{
    return &Director{firstName, lastName}
}

func newPromise(yearsLeft int, wage int) *Promise{
    return &Promise{yearsLeft, wage}
}

type Employee struct{
    id int
    firstName string
    lastName string
    promise Promise
    money int
}

func newEmployee(id int, firstName string, lastName string, yearsLeft int, wage int, money int) *Employee{
    return &Employee{id, firstName, lastName, *newPromise(yearsLeft, wage), money}
}

type Company struct{
    money int
    director Director
    employees [] *Employee
}

func newCompany(money int, director Director, employees [] *Employee) *Company{
    return &Company{money, director, employees}
}

func (c *Company) earn(flot int){
    c.money+=flot
}

func (c *Company) payWage(){
    for _, el := range c.employees{
        if(c.money >= el.promise.wage){
            c.money -= el.promise.wage
            el.money += el.promise.wage
        } else {
            fmt.Println("Money left. Sorry bro")
            return
        }
    }
}

func (c *Company) printCompany(){
    fmt.Println("Money:", c.money)
    fmt.Println("Director:", c.director)
    fmt.Println("Employees:")
    for i := 0; i < len(c.employees); i++{
        fmt.Println(c.employees[i])
    }
}


func main(){
    director := newDirector("Victor", "Drobysh")

    employees := [] *Employee{
        newEmployee(1, "Ivan", "Drobysh", 10, 500000, 1000000),
        newEmployee(2, "Dmitry", "Drobysh", 10, 500000, 20000)}

    company := newCompany(1000000000, *director, employees)

    company.printCompany()
    fmt.Println()

    company.earn(500000)

    company.printCompany()
    fmt.Println()

    company.payWage()

    company.printCompany()
}
