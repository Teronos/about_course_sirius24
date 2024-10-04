from typing import List

from tasks.task10.Company.AbstractEmployee import AbstractEmployee
from tasks.task10.Company.Promise import Promise

class Director(AbstractEmployee):
    __subordinates: List[AbstractEmployee]

    def __init__(
            self,
            employee_id: int,
            first_name: str,
            second_name: str,
            __insurance_number: str,
            promise: Promise,
            subordinates = None
    ):
        super().__init__(
            employee_id,
            first_name,
            second_name,
            __insurance_number,
            promise
        )

        if subordinates is None:
            subordinates = []
        self.__subordinates = subordinates

    def get_subordinates(self) -> List[AbstractEmployee]:
        return self.__subordinates

    def add_employee_to_subordinate(self, employee: AbstractEmployee):
        self.__subordinates.append(employee)

    def remove_employee_from_subordinate(self, employee: AbstractEmployee):
        self.__subordinates.remove(employee)