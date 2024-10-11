#Нужно создать функционал для упрошенного описания экономических отношений между работодателем, работником и компанией. 
#Нужно реализовать классы Director, Employee, Company, Promise.

#У компании должен быть метод, позволяющей получить прибыль условных единиц (flot). У Компании всегда есть только один Director, количество Employee не ограниченно. 
#Также у компании должен быть метод позволяющий начислить зарплату всем ее работникам, согласно Promise каждого сотрудника компании.

#У всех работников компании есть контракт с компанией о размере его заработной плате – Promise, а также есть имена, фамилии и номера СНИЛС(Id)

#Promise - содержит в себе СНИЛС(Id) работника, размер его зарабтной платы, и информацию о том, была ли начисленна плата сотруднику

#fulfill_promise – метод, начисялющий всем заработную плату согласно персональному Promise каждого работника, если это возможно. Возвращает булевое значение


 # Создаем класс Promise
class Promise: 
    def __init__(self, id, salary): 
        self.id = id 
        self.salary = salary 
        self.is_paid = False  # Покажет, была ли выплачена зп

 # Функция, проверяет выплачена зп или нет и возвращает размер зп
    def fulfill(self, balance): 
        if balance >= self.salary: 
            self.paid = True 
            return self.salary 
        self.paid = False 
        return 0 
 
 # Создаем класс Employee
class Employee: 

    def __init__(self, first_name, second_name, id, salary): 
        self.first_name = first_name 
        self.second_name = second_name 
        self.id = id 
        self.promise = Promise(id, salary) 

# Создаем класс Director   
class Director(Employee): 
    def __init__(self, first_name, second_name, id, salary): 
        super().__init__(first_name, second_name, id, salary) 
 

 # Функция, которая проверяет все ли обещания были выполнены
    def check_promises(self, company): 
        return all(promise.paid for promise in company.promises)


 # Создаем класс Company
class Company: 
    def __init__(self, balance): 
        self.balance = balance 
        self.director = None 
        self.employees = [] 
        self.promises = [] 
 
 # Функция, которая создаст директора
    def create_director(self, first_name, second_name, id, salary): 
        self.director = Director(first_name, second_name, id, salary) 
        self.promises.append(self.director.promise) 
 
  # Функция, которая создаст сотрудника
    def create_employee(self, first_name, second_name, id, salary): 
        employee = Employee(first_name, second_name, id, salary) 
        self.employees.append(employee) 
        self.promises.append(employee.promise) 
 
 # Функция, которая устанавливает прибыль компании
    def set_profit(self, summ): 
        self.balance += summ 
 
    def fulfill_promise(self): 
        # Сбрасываем статус "is_paid" перед началом выполнения 
        for i in self.promises: 
            i.paid = False 
        all_summ = 0 
        for i in self.promises: 
            salary_paid = i.fulfill(self.balance) 
            all_summ += salary_paid 
            self.balance -= salary_paid 
 
        return all_summ > 0 
 
### ПРОВЕРКА РАБОТЫ ###

vk = Company(balance=50) 
 
 
vk.create_director( 
    first_name="Владимир", 
    second_name="Кириенко", 
    id=1, 
    salary=15 
) 
 
 
vk.create_employee( 
    first_name="Елена", 
    second_name="Иванова", 
    id=2, 
    salary=8 
) 
 
vk.create_employee( 
    first_name="Виктор", 
    second_name="Кузнецов", 
    id=3, 
    salary=6 
) 
 
# Устанавливаем прибыль компании 
vk.set_profit(145.12) 
 
# Выполняем обещания по зп 
vk.fulfill_promise() 
 
# Проверяем, выполнены ли обещания по зп директора 
director = vk.director 
print(director.check_promises(vk))  # True 
 
# Устанавливаем убыток компании 
vk.set_profit(-200) 
 
# Снова выполняем обещания по зп 
vk.fulfill_promise() 
 
# Проверяем, выполнены ли обещания по зп директора после убытков 
print(director.check_promises(vk))  # False
 


