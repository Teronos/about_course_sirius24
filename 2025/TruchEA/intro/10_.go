package main

import "fmt"

// Promise представляет контракт о заработной плате
type Promise struct {
	ID        int
	Salary    float64
	Fulfilled bool
}

// NewPromise создает новый Promise
func NewPromise(id int, salary float64) *Promise {
	return &Promise{
		ID:        id,
		Salary:    salary,
		Fulfilled: false,
	}
}

// Employee представляет работника компании
type Employee struct {
	FirstName  string
	SecondName string
	ID         int
	Promise    *Promise
}

// NewEmployee создает нового работника
func NewEmployee(firstName, secondName string, id int, salary float64) *Employee {
	return &Employee{
		FirstName:  firstName,
		SecondName: secondName,
		ID:         id,
		Promise:    NewPromise(id, salary),
	}
}

// CheckPromise проверяет, выполнено ли обещание по зарплате
func (e *Employee) CheckPromise() bool {
	return e.Promise.Fulfilled
}

// Director представляет директора компании
type Director struct {
	Employee
}

// NewDirector создает нового директора
func NewDirector(firstName, secondName string, id int, salary float64) *Director {
	return &Director{
		Employee: *NewEmployee(firstName, secondName, id, salary),
	}
}

// CheckPromises проверяет, выполнены ли все обещания по зарплате
func (d *Director) CheckPromises() bool {
	return d.CheckPromise()
}

// Company представляет компанию
type Company struct {
	balance   float64
	director  *Director
	employees []*Employee
}

// NewCompany создает новую компанию
func NewCompany(balance float64) *Company {
	return &Company{
		balance:   balance,
		employees: make([]*Employee, 0),
	}
}

// CreateDirector создает директора компании
func (c *Company) CreateDirector(firstName, secondName string, id int, salary float64) {
	c.director = NewDirector(firstName, secondName, id, salary)
}

// CreateEmployee создает работника компании
func (c *Company) CreateEmployee(firstName, secondName string, id int, salary float64) {
	employee := NewEmployee(firstName, secondName, id, salary)
	c.employees = append(c.employees, employee)
}

// SetProfit устанавливает прибыль компании
func (c *Company) SetProfit(profit float64) {
	c.balance = profit
}

// FulfillPromise начисляет зарплату всем работникам
func (c *Company) FulfillPromise() bool {
	// Рассчитываем общую сумму зарплат
	totalSalary := 0.0

	// Добавляем зарплату директора
	if c.director != nil {
		totalSalary += c.director.Promise.Salary
	}

	// Добавляем зарплаты всех работников
	for _, employee := range c.employees {
		totalSalary += employee.Promise.Salary
	}

	// Проверяем, хватает ли средств
	if c.balance < totalSalary {
		// Сбрасываем статус выполнения обещаний
		if c.director != nil {
			c.director.Promise.Fulfilled = false
		}
		for _, employee := range c.employees {
			employee.Promise.Fulfilled = false
		}
		return false
	}

	// Выплачиваем зарплаты
	if c.director != nil {
		c.director.Promise.Fulfilled = true
		c.balance -= c.director.Promise.Salary
	}

	for _, employee := range c.employees {
		employee.Promise.Fulfilled = true
		c.balance -= employee.Promise.Salary
	}

	return true
}

// Director возвращает директора компании
func (c *Company) Director() *Director {
	return c.director
}

// GetBalance возвращает текущий баланс компании
func (c *Company) GetBalance() float64 {
	return c.balance
}

func main() {
	// Пример использования
	vk := NewCompany(50)

	vk.CreateDirector(
		"Владимир",
		"Кириенко",
		1,
		15,
	)

	vk.CreateEmployee(
		"Елена",
		"Иванова",
		2,
		8,
	)

	vk.CreateEmployee(
		"Виктор",
		"Кузнецов",
		3,
		6,
	)

	vk.SetProfit(145.12)
	result1 := vk.FulfillPromise()

	director := vk.Director()
	fmt.Printf("Первое выполнение обещаний: %v\n", result1)
	fmt.Printf("Директор проверяет обещания: %v\n", director.CheckPromises())

	vk.SetProfit(-200)
	result2 := vk.FulfillPromise()

	fmt.Printf("Второе выполнение обещаний: %v\n", result2)
	fmt.Printf("Директор проверяет обещания: %v\n", director.CheckPromises())

	// Дополнительная проверка для работников
	fmt.Printf("Елена Иванова получила зарплату: %v\n", vk.employees[0].CheckPromise())
	fmt.Printf("Виктор Кузнецов получил зарплату: %v\n", vk.employees[1].CheckPromise())
}
