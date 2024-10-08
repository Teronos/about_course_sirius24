import random
from sample.task_10.director import Director
from sample.task_10.employee import Employee


class Company:

    name: str
    profit: float
    director: Director
    employees: list[Employee] = list()

    def __init__(self, name, profit):
        self.name = name
        self.profit = profit

    def set_director(self, director):
        self.director = director

    def add_employee(self, employee):
        self.employees.append(employee)

    def collect_profit(self):
        randomProfit = random.randrange(0, 500)
        self.profit += randomProfit
        print("Earned: " + str(randomProfit))

    def get_profit(self):
        print("Profit: " + str(self.profit))

    def show_employees(self):
        print("Employees: ")
        for e in self.employees:
            print(e.name)

    def show_info(self):
        print("Company name: " + self.name)
        print("Director: " + self.director.name)

    def fulfill_promise(self):
        paidSum = 0
        for e in self.employees:
            self.profit -= e.promise.promise
            e.promise.paid = True
            paidSum += e.promise.promise
            if self.profit <= 0:
                print("Your budget is run out!")
                exit(0)
        print("Paid: " + str(paidSum))

