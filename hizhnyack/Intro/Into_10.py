class Promise:
    def __init__(self, salary: int):
        self.salary = salary

    def __int__(self) -> int:
        return self.salary
    def __int__(cls, value: int)-> 'Promise':
        return Promise(value)


class People:
    def __init__(self, first_name, second_name, ID:int, salary:Promise):
        self.first_name = first_name
        self.second_name = second_name
        self.ID = ID
        self.salary = salary
        self.is_paid = False

class Director(People):
    def __init__(self, first_name, second_name, ID:int, salary:Promise):
        super().__init__(first_name, second_name, ID, salary)
    def check_promises(self):
        return self.is_paid


class Company:
    def __init__(self, balance:int):
        self.balance = balance
        self.employee = []
        self.director = None

    def create_director(self,first_name, second_name):
        self.director = Director(first_name,second_name,0,10)

    def create_employee(self,first_name, second_name, ID:int, salary:Promise):
        self.employee.append(People(first_name,second_name,ID,salary))

    def set_profit(self,new_balance:int):
        self.balance += new_balance
        for emp in self.employee:
            emp.is_paid = False
        if self.director is not None:
            self.director.is_paid = False

    def fullfill_promise(self):
        total_salary = 0
        if self.director is not None:
            total_salary += self.director.salary
        for emp in self.employee:
            total_salary += emp.salary
        if self.balance < total_salary:
            return False
        self.balance = self.balance - total_salary
        for emp in self.employee:
            emp.is_paid = True
        if self.director is not None:
            self.director.is_paid = True
        return True



vk = Company(balance=50)
vk.create_director(
  first_name = "Владимир",
  second_name = "Кириенко",
  )

vk.create_employee(
  first_name = "Елена",
  second_name = "Иванова",
  ID = 2,
  salary = 8
)

vk.create_employee(
  first_name = "Виктор",
  second_name = "Кузнецов",
  ID = 3,
  salary = 6
)

vk.set_profit(145.12)
vk.fullfill_promise()

director = vk.director
print(director.check_promises()) # true

vk.set_profit(-200)
vk.fullfill_promise()

print(director.check_promises()) # true








