#Задача 10*
#Нужно создать функционал для упрошенного описания экономических отношений между работодателем, работником и компанией. Нужно реализовать классы Director, Employee, Company, Promise.
#У компании должен быть метод, позволяющей получить прибыль условных единиц (flot). У Компании всегда есть только один Director, количество Employee не ограниченно. Также у компании должен быть метод позволяющий начислить зарплату всем ее работникам, согласно Promise каждого сотрудника компании.
#У всех работников компании есть контракт с компанией о размере его заработной плате – Promise, а также есть имена, фамилии и номера СНИЛС(Id)
#Promise - содержит в себе СНИЛС(Id) работника, размер его зарабтной платы, и информацию о том, была ли начисленна плата сотруднику
#fulfill_promise – метод, начисялющий всем заработную плату согласно персональному Promise каждого работника, если это возможно. Возвращает булевое значение


class Promise:
    def __init__(self, employee_id: int, salary: float) -> None:
        self.employee_id: int = employee_id
        self.salary: float = salary
        self.is_paid: bool = False

    def fulfill(self, balance: float) -> float:
        if balance >= self.salary:
            self.is_paid = True
            return self.salary
        self.is_paid = False
        return 0.0


class Employee:
    def __init__(self, first_name: str, second_name: str, employee_id: int, salary: float) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.id: int = employee_id
        self.promise: Promise = Promise(employee_id, salary)


class Director(Employee):
    def __init__(self, first_name: str, second_name: str, employee_id: int, salary: float) -> None:
        super().__init__(first_name, second_name, employee_id, salary)

    def check_promises(self, company: "Company") -> bool:
        return all(promise.is_paid for promise in company.promises)


class Company:
    def __init__(self, balance: float) -> None:
        self.balance: float = balance
        self.director: Director | None = None
        self.employees: list[Employee] = []
        self.promises: list[Promise] = []

    def create_director(self, first_name: str, second_name: str, employee_id: int, salary: float) -> None:
        self.director = Director(first_name, second_name, employee_id, salary)
        self.promises.append(self.director.promise)

    def create_employee(self, first_name: str, second_name: str, employee_id: int, salary: float) -> None:
        employee = Employee(first_name, second_name, employee_id, salary)
        self.employees.append(employee)
        self.promises.append(employee.promise)

    def set_profit(self, amount: float) -> None:
        self.balance += amount

    def fulfill_promise(self) -> bool:
        for promise in self.promises:
            promise.is_paid = False

        total_salaries = 0.0
        for promise in self.promises:
            salary_paid = promise.fulfill(self.balance)
            total_salaries += salary_paid
            self.balance -= salary_paid

        return total_salaries > 0

# Проверка
vk = Company(balance=50.0)

vk.create_director(
    first_name="Владимир",
    second_name="Кириенко",
    employee_id=1,
    salary=15.0
)

vk.create_employee(
    first_name="Елена",
    second_name="Иванова",
    employee_id=2,
    salary=8.0
)

vk.create_employee(
    first_name="Виктор",
    second_name="Кузнецов",
    employee_id=3,
    salary=6
)

vk.set_profit(145.12)
vk.fulfill_promise()

director = vk.director
print(director.check_promises(vk))  # True

vk.set_profit(-200.0)
vk.fulfill_promise()

print(director.check_promises(vk))  # False