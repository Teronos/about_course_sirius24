import random

from tasks.task10.Company.AbstractEmployee import AbstractEmployee
from tasks.task10.Company.DefaultEmployee import DefaultEmployee
from tasks.task10.Company.Director import Director
from tasks.task10.Company.EmployeeIdGenerator import EmployeeIdGenerator
from tasks.task10.Company.Promise import Promise


class Company:
    __director: Director
    __balance: float
    __name: str
    __employee_id_generator: EmployeeIdGenerator = EmployeeIdGenerator()

    def __init__(
            self,
            name: str,
            balance: float = 0,
            director: Director = None,
    ):
        self.__name = name
        self.__balance = balance
        self.__director = director

    def get_balance(self):
        return self.__balance

    def create_director(
            self,
            first_name: str,
            second_name: str,
            salary: float,
    ) -> Director:
        if self.__director:
            raise ValueError(
                "There is already a director in this company, you must have made a mistake!"
            )

        self.__director = Director(
            self.__employee_id_generator.generate_id_for_user(),
            first_name,
            second_name,
            str(random.randint(10 ** 14, 10 ** 15 - 1)),
            Promise(salary)
        )

        return self.__director

    def create_employee(
            self,
            first_name: str,
            second_name: str,
            salary: float,
    ) -> DefaultEmployee:
        if not self.__director:
            raise ValueError("There is no director who can hire an employee!")

        new_employee = DefaultEmployee(
            self.__employee_id_generator.generate_id_for_user(),
            first_name,
            second_name,
            str(random.randint(10 ** 14, 10 ** 15 - 1)),
            Promise(salary)
        )

        self.__director.add_employee_to_subordinate(new_employee)

        return new_employee

    def set_profit(self, count: float) -> float:
        self.__balance += count

        return self.__balance

    def fulfill_promise(self) -> None:
        for employee in self.__director.get_subordinates():
            self.fulfill_or_debt_promise_for_employee(employee)

        self.fulfill_or_debt_promise_for_employee(self.__director)

    def fulfill_or_debt_promise_for_employee(self, employee: AbstractEmployee) -> None:
        employee_salary = employee.get_promise().get_salary()

        if self.__balance - employee_salary < 0:
            employee.get_promise().set_company_debt(employee_salary)

        self.__balance -= employee_salary

        employee.set_balance(employee_salary)