#Задание 10*
class Promise:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
        self.paid = False


class Employee:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.promise = Promise(employee_id, salary)


class Director:
    def __init__(self, first_name, last_name, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id


class Company:
    def __init__(self, director):
        self.director = director
        self.employees = []
        self.profit = 0

    def set_profit(self, profit):
        self.profit = profit
        return self.fulfill_promise()

    def add_employee(self, employee):
        self.employees.append(employee)

    def fulfill_promise(self):
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

employee1 = Employee("Petr", "Petrov", "987-65-4321", 5000)
employee2 = Employee("Anna", "Sidorova", "654-32-1987", 7000)

company.add_employee(employee1)
company.add_employee(employee2)

# Устанавливаем прибыль компании
if company.set_profit(12000):
    print("Зарплата успешно начислена всем сотрудникам.")
else:
    print("Недостаточно средств для выплаты зарплаты.")
