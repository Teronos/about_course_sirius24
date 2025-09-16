from tasks.task10.Company.AbstractEmployee import AbstractEmployee
from tasks.task10.Company.Promise import Promise


class DefaultEmployee(AbstractEmployee):
    def __init__(
            self,
            employee_id: int,
            first_name: str,
            second_name: str,
            __insurance_number: str,
            promise: Promise
    ):
        super().__init__(
            employee_id,
            first_name,
            second_name,
            __insurance_number,
            promise
        )