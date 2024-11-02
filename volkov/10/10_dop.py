

class Promise:
    def __init__(self, employee_id: int, salary: float):
        self.employee_id = employee_id
        self.salary = salary
        self.is_fulfilled = False  # Был ли выплачен Promise

    def fulfill(self) -> bool:
        """Выплачивает обещанную зарплату."""
        if not self.is_fulfilled:
            self.is_fulfilled = True
            return True
        return False

    def __repr__(self):
        return f"Promise(Id={self.employee_id}, salary={self.salary}, fulfilled={self.is_fulfilled})"


class Employee:
    def __init__(self, first_name: str, second_name: str, employee_id: int, salary: float):
        self.first_name = first_name
        self.second_name = second_name
        self.employee_id = employee_id
        self.promise = Promise(employee_id, salary)

    def __repr__(self):
        return f"Employee({self.first_name} {self.second_name}, Id={self.employee_id}, salary={self.promise.salary})"


class Director(Employee):
    def __repr__(self):
        return f"Director({self.first_name} {self.second_name}, Id={self.employee_id}, salary={self.promise.salary})"


class Company:
    def __init__(self, balance: float):
        self.balance = balance
        self._director = None
        self.employees = []

    def create_director(self, first_name: str, second_name: str, employee_id: int, salary: float):
        """Создает директора компании."""
        self._director = Director(first_name, second_name, employee_id, salary)

    def create_employee(self, first_name: str, second_name: str, employee_id: int, salary: float):
        """Добавляет нового сотрудника."""
        employee = Employee(first_name, second_name, employee_id, salary)
        self.employees.append(employee)

    def set_profit(self, amount: float):
        """Изменяет баланс компании, добавляя прибыль."""
        self.balance += amount

    def fulfill_promise(self) -> bool:
        """Выполняет выплаты зарплат сотрудникам."""
        total_salaries = sum(employee.promise.salary for employee in self.employees)

        if self._director:
            total_salaries += self._director.promise.salary

        if self.balance >= total_salaries:
            for employee in self.employees:
                employee.promise.fulfill()
            if self._director:
                self._director.promise.fulfill()
            self.balance -= total_salaries
            return True
        else:
            return False

    def check_promises(self) -> bool:
        """Проверяет, выполнены ли обещания выплаты для всех сотрудников."""
        all_fulfilled = all(employee.promise.is_fulfilled for employee in self.employees)
        if self._director:
            all_fulfilled = all_fulfilled and self._director.promise.is_fulfilled
        return all_fulfilled

    def director(self):
        """Возвращает директора компании."""
        return self._director

    def __repr__(self):
        return f"Company(balance={self.balance}, employees={len(self.employees)})"


# Пример использования
vk = Company(balance=50)

vk.create_director(
    first_name="loool1",
    second_name="loool2",
    employee_id=1,
    salary=15
)

vk.create_employee(
    first_name="Oleg1",
    second_name="Oleg2",
    employee_id=2,
    salary=8
)

vk.create_employee(
    first_name="Виктор1",
    second_name="Виктор2",
    employee_id=3,
    salary=6
)

vk.set_profit(145.12)
print(vk.fulfill_promise())  # True (успешная выплата зарплат)

print(vk.check_promises())  # True (выплаты прошли успешно)

vk.set_profit(-200)
print(vk.fulfill_promise())  # False (недостаточно средств для выплат)

print(vk.check_promises())  # False (зарплаты не выплачены)
