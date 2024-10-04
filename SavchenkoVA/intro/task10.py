from enum import Enum
from numbers import Number

"""
Задача 10:
Нужно спроектировать систему платформы электронного обучения.
В ней есть администраторы системы, преподаватели курсов и студенты.
"""


class Role(Enum):
    Administrators = 1
    Teacher = 2
    Student = 3


class User:
    last_name: str
    first_name: str
    login: str
    __role: Role
    __password: str

    def __init__(self, last_name: str, first_name: str, login: str, password: str, role: Role) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.login = login
        self.__password = password
        self.__role = role

    def greeting(self) -> None:
        print('Добро пожаловать,', self.first_name, self.last_name)
        print('Ваш логин:', self.login)
        print('Ваш пароль:', '*' * len(self.__password))
        print('Ваша роль:', self.__role)


def task10() -> None:
    admin = User('Vova', 'Ivanov', 'vov_ivan', '124ddfdf', Role.Administrators)
    admin.greeting()
    student = User('Vova', 'Ivanov', 'vov_ivan', '124ddfdf', Role.Student)
    student.greeting()
    teacher = User('Vova', 'Ivanov', 'vov_ivan', '124ddfdf', Role.Teacher)
    teacher.greeting()


"""
Задача 10*:
Нужно создать функционал для упрошенного описания экономических отношений между работодателем,
работником и компанией. Нужно реализовать классы Director, Employee, Company, Promise.
У компании должен быть метод, позволяющей получить прибыль условных единиц (float).
У Компании всегда есть только один Director, количество Employee не ограниченно.
Также у компании должен быть метод позволяющий начислить зарплату всем ее работникам,
согласно Promise каждого сотрудника компании.
У всех работников компании есть контракт с компанией о размере его заработной плате – Promise,
а также есть имена, фамилии и номера СНИЛС(Id)
"""


class Promise:
    promise: Number

    def __init__(self, promise: Number) -> None:
        self.promise = promise


class Director:
    second_name: str
    first_name: str
    Id: int
    salary: Number
    promise: Promise

    def __init__(self, first_name: str, second_name: str, Id: int, salary: Number) -> None:
        self.second_name = second_name
        self.first_name = first_name
        self.Id = Id
        self.salary = salary
        self.promise = Promise(salary)

    def check_promises(self) -> bool:
        return self.salary >= self.promise.promise


class Employee:
    second_name: str
    first_name: str
    Id: int
    salary: Number
    promise: Promise

    def __init__(self, first_name: str, second_name: str, Id: int, salary: Number) -> None:
        self.second_name = second_name
        self.first_name = first_name
        self.Id = Id
        self.salary = salary
        self.promise = Promise(salary)


class Company:
    balance: Number
    __director: Director
    __employees: list[Employee]

    def __init__(self, balance: Number = 0) -> None:
        self.balance = balance
        self.__director = Director('', '', 0, 0)
        self.__employees = list()

    def create_director(self, first_name: str = '', second_name: str = '', Id: int = 0, salary: Number = 0) -> None:
        self.__director = Director(first_name, second_name, Id, salary)

    def create_employee(self, first_name: str = '', second_name: str = '', Id: Number = 0, salary: Number = 0) -> None:
        employee = Employee(first_name, second_name, Id, salary)
        self.__employees.append(employee)

    def set_profit(self, profit: Number) -> None:
        self.__director.salary = profit
        for i in range(len(self.__employees)):
            self.__employees[i].salary = profit

    def fulfill_promise(self) -> None:
        pass

    def director(self) -> Director:
        return self.__director


def task10_p() -> None:
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
    vk.fulfill_promise()

    director = vk.director()
    print("director.check_promises:", director.check_promises())  # true

    vk.set_profit(-200)
    vk.fulfill_promise()

    print("director.check_promises:", director.check_promises())  # false


if __name__ == "__main__":
    print('Задача 10:')
    task10()
    print('\nЗадача 10*:')
    task10_p()
