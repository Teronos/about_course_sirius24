import abc

from tasks.task10.Company.Promise import Promise
from tasks.task10.General.Citizen import Citizen

class AbstractEmployee(Citizen, metaclass=abc.ABCMeta):
    __id: int

    __promise: 'Promise'

    def __init__(
            self,
            employee_id: int,
            first_name: str,
            second_name: str,
            __insurance_number: str,
            promise: Promise
    ):
        super().__init__(first_name, second_name, __insurance_number)
        self.__id = employee_id
        self.__promise = promise

    def get_promise(self) -> Promise:
        return self.__promise

    def check_promises(self) -> bool:
        return self.__promise.get_company_debt() == 0
