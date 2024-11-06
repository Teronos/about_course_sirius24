from tasks.task10.General import AbstractHuman

class Citizen(AbstractHuman.AbstractHuman):
    __insurance_number: str
    __balance: float

    def __init__(
            self,
            first_name: str,
            second_name: str,
            __insurance_number: str,
            __balance: float = 0,
    ):
        super().__init__(first_name, second_name)
        self.__insurance_number = __insurance_number
        self.__balance = __balance

    def get_insurance_number(self) -> str:
        return self.__insurance_number

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float) -> float:
        self.__balance += balance

        return self.__balance