# Нужно создать функционал для упрошенного описания экономических отношений между работодателем, работником и компанией.
# Нужно реализовать классы Director, Employee, Company, Promise.
#
# У компании должен быть метод, позволяющей получить прибыль условных единиц (flot).
# У компании всегда есть только один Director, количество Employee не ограниченно.
# Также у компании должен быть метод позволяющий начислить зарплату всем ее работникам,
# согласно Promise каждого сотрудника компании.
#
# У всех работников компании есть контракт с компанией о размере его заработной плате – Promise,
# а также есть имена, фамилии и номера СНИЛС(Id)
#
# Promise - содержит в себе СНИЛС(Id) работника, размер его заработной платы, и информацию о том,
# была ли начислена плата сотруднику
#
# set_profit - метод, устанавливающий прибыль всей компании за некоторый промежуток времен.
#
# fulfill_promise – метод, начисляющий всем заработную плату согласно персональному Promise каждого работника,
# если это возможно. Возвращает булевое значение
#
# Замечание: метод set_profit устанавливает прибыль для компании. Компания в свою очередь, пытается выплатить
# заработную плату всем сотрудникам компании методом fulfill_promise. Если баланса компании хватает на выплаты
# всем участникам компании, то fulfill_promise возвращает true, в противном случае false


class Promise:
    def __init__(self, id_, salary):
        self.id = id_
        self.salary = salary
        self.fulfilled = False

    def mark_fulfilled(self):
        self.fulfilled = True

    def start_new_fulfillment_period(self):
        self.fulfilled = False

    def is_fulfilled(self):
        return self.fulfilled


class Employee:
    def __init__(self, first_name, second_name, id_, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.id = id_
        self.salary = salary
        self.promise = Promise(id_, salary)


class Director(Employee):
    def __init__(self, first_name, second_name, id_, salary):
        super().__init__(first_name, second_name, id_, salary)

    def check_promises(self):
        return self.promise.is_fulfilled()


class Company:
    def __init__(self, balance=0.0):
        self.balance = float(balance)
        self.__director = None
        self.employees = []

    def create_director(self, first_name, second_name, id_, salary):
        director = Director(first_name, second_name, id_, salary)
        self.__director = director
        self.employees.append(director)

    def create_employee(self, first_name, second_name, id_, salary):
        employee = Employee(first_name, second_name, id_, salary)
        self.employees.append(employee)

    def set_profit(self, profit):
        self.balance += float(profit)

    def fulfill_promise(self):
        for emp in self.employees:
            emp.promise.start_new_fulfillment_period()

        total_salary = sum(emp.promise.salary for emp in self.employees)

        if self.balance < total_salary:
            return False

        for emp in self.employees:
            self.balance -= emp.promise.salary
            emp.promise.mark_fulfilled()
        return True

    def director(self):
        return self.__director


vk = Company(balance=50)
vk.create_director(
  first_name = "Владимир",
  second_name = "Кириенко",
  id_ = 1,
  salary = 15
)

vk.create_employee(
  first_name = "Елена",
  second_name = "Иванова",
  id_ = 2,
  salary = 8
)

vk.create_employee(
  first_name = "Виктор",
  second_name = "Кузнецов",
  id_ = 3,
  salary = 6
)

vk.set_profit(145.12)
vk.fulfill_promise()

director = vk.director()
print(director.check_promises())

vk.set_profit(-200)
vk.fulfill_promise()
print(director.check_promises())