class Promise:
    __salary: float
    __company_debt: float

    def __init__(
            self,
            salary: float,
            company_debt: float = 0
    ):
        self.__salary = salary
        self.__company_debt = company_debt

    def get_salary(self) -> float:
        return self.__salary

    def set_company_debt(self, company_debt: float) -> float:
        self.__company_debt += company_debt

        return self.__company_debt

    def get_company_debt(self) -> float:
        return self.__company_debt