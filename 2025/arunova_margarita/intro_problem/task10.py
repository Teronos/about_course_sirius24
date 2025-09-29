"""
Нужно создать функционал для упрощенного описания экономических отношений между работодателем, работником и компанией.
Нужно реализовать классы Director, Employee, Company, Promise.

У Company должен быть метод, позволяющей получить прибыль условных единиц (flot).
У Company всегда есть только один Director, количество Employee не ограниченно.
Также у Company должен быть метод позволяющий начислить зарплату всем ее Employee, согласно Promise каждого сотрудника компании.

У всех Employee в Company есть контракт с компанией о размере его заработной плате – Promise, а также есть имена, фамилии и номера СНИЛС(Id)

Promise - содержит в себе СНИЛС(Id) работника, размер его зарабтной платы, и информацию о том, была ли начисленна плата сотруднику

* set_profit - метод, устанваливающий прибыль всей компании за некоторый промежуток времен.
* fulfill_promise – метод, начисялющий всем заработную плату согласно персональному Promise каждого работника, если это возможно. Возвращает булевое значение

Замечание: метод set_profit устанавливает прибыль для Company.
Company в свою очередь, пытается выплатить заработную плату всем сотрудникам компании методом fulfill_promise.
Если баланса компании хватает на выплаты всем участникам компании, то fulfill_promise возвращает true, в противном случаее false
"""


class Promise:
    def __init__(self, id: int, salary: float):
        self.__id = id
        self.salary = salary
        self.is_paid = False

    def set_paid(self, flag):
        self.is_paid = flag


class Employee:
    def __init__(self, first_name: str, second_name: str, id: int, salary: float):
        self.__id = id
        self.__first_name = first_name
        self.__second_name = second_name
        self.promise = Promise(id, salary)


class Director(Employee):
    def __init__(self, first_name: str, second_name: str, id: int, salary: float):
        super().__init__(first_name, second_name, id, salary)

    def check_promises(self, company = None) -> bool:
        if company:
            return all(employee.promise.is_paid for employee in company.__employees + [company.__director])
        return self.promise.is_paid


class Company:
    def __init__(self, balance: float = 0.0):
        self.__balance = balance
        self.__employees = []
        self.__director = None

    def director(self):
        return self.__director

    def create_director(self, first_name: str, second_name: str, Id: int, salary: float):
        if self.__director is not None:
            raise ValueError("У компании может быть только один директор :)")
        self.__director = Director(first_name, second_name, Id, salary)
        return self.__director

    def create_employee(self, first_name: str, second_name: str, Id: int, salary: float) -> Employee:
        employee = Employee(first_name, second_name, Id, salary)
        self.__employees.append(employee)
        return employee

    def set_profit(self, profit: float):
        self.__balance = profit

    def fulfill_promise(self):
        employees = [self.__director] + self.__employees
        salary_sum = sum(worker.promise.salary for worker in employees)

        is_paid = False
        if self.__balance >= salary_sum:
            is_paid = True
            self.__balance -= salary_sum
        for employee in employees:
            employee.promise.set_paid(is_paid)
        return is_paid



vk = Company(balance=50)
vk.create_director(
    first_name="Владимир",
    second_name="Кириенко",
    Id=1,
    salary=15
)

vk.create_employee(
    first_name="Елена",
    second_name="Иванова",
    Id=2,
    salary=8
)

vk.create_employee(
    first_name="Виктор",
    second_name="Кузнецов",
    Id=3,
    salary=6
)

vk.set_profit(145.12)
print(vk.fulfill_promise())

director = vk.director()
print(director.check_promises())  # true

vk.set_profit(-200)
print(vk.fulfill_promise())

print(director.check_promises())  # false
