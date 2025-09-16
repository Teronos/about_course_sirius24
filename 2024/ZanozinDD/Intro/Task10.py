#Задание 10*
class Promise:
    def __init__(self, employee_id: str, salary: float) -> None:
        self.employee_id = employee_id
        self.salary = salary
        self.paid = False


class Employee:
    def __init__(self, first_name: str, last_name: str, employee_id: str, salary: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.promise = Promise(employee_id, salary)


class Director:
    def __init__(self, first_name: str, last_name: str, employee_id: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id


class Company:
    def __init__(self, director: Director) -> None:
        self.director = director
        self.employees = []
        self.profit = 0.0

    def set_profit(self, profit: float) -> bool:
        self.profit = profit
        return self.fulfill_promise()

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def fulfill_promise(self) -> bool:
        total_salary = sum(emp.promise.salary for emp in self.employees)

        if total_salary <= self.profit:
            for emp in self.employees:
                emp.promise.paid = True
            self.profit -= total_salary
            return True
        return False


# Пример использования
director = Director("Ivan", "Ivanov", "123-45-6789")
company = Company(director)

employee1 = Employee("Petr", "Petrov", "987-65-4321", 5000.0)
employee2 = Employee("Anna", "Sidorova", "654-32-1987", 7000.0)

company.add_employee(employee1)
company.add_employee(employee2)

# Устанавливаем прибыль компании
if company.set_profit(12000.0):
    print("Зарплата успешно начислена всем сотрудникам.")
else:
    print("Недостаточно средств для выплаты зарплаты.")

