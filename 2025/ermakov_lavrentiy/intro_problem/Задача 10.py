class Promise:
    def __init__(self, worker_id, salary):
        self.worker_id = worker_id
        self.salary = salary
        self.is_fulfilled = False

class Worker:
    def __init__(self, first_name, second_name, worker_id, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.id = worker_id
        self.promise = Promise(worker_id, salary)
    
    def check_promises(self):
        """Проверяет, был ли выполнен Promise"""
        return self.promise.is_fulfilled

class Director(Worker):
    pass

class Employee(Worker):
    pass

class Company:
    def __init__(self, balance=0):
        self.balance = float(balance)
        self._director = None
        self.employees = []
    
    def create_director(self, first_name, second_name, Id, salary):
        """Создает директора компании"""
        self._director = Director(first_name, second_name, Id, salary)
        return self._director
    
    def create_employee(self, first_name, second_name, Id, salary):
        """Создает сотрудника компании"""
        employee = Employee(first_name, second_name, Id, salary)
        self.employees.append(employee)
        return employee
    
    def director(self):
        """Возвращает директора компании"""
        return self._director
    
    def set_profit(self, profit):
        """Устанавливает прибыль компании (может быть отрицательной)"""
        self.balance += float(profit)
    
    def fulfill_promise(self):
        """
        Начисляет зарплату всем работникам, если хватает средств.
        Возвращает boolean результат.
        """
        if not self._director:
            return False
        
        # Собираем всех работников
        all_workers = [self._director] + self.employees
        
        # Проверяем, все ли Promise уже выполнены
        all_fulfilled = all(worker.promise.is_fulfilled for worker in all_workers)
        if all_fulfilled:
            return True
        
        # Рассчитываем общую сумму для выплаты
        total_salary = 0
        for worker in all_workers:
            if not worker.promise.is_fulfilled:
                total_salary += worker.promise.salary
        
        # Проверяем, хватает ли средств
        if self.balance >= total_salary:
            # Выплачиваем зарплаты
            for worker in all_workers:
                if not worker.promise.is_fulfilled:
                    worker.promise.is_fulfilled = True
            self.balance -= total_salary
            return True
        else:
            # Не хватает средств - сбрасываем все Promise
            for worker in all_workers:
                worker.promise.is_fulfilled = False
            return False

# Пример использования из задания
if __name__ == "__main__":
    vk = Company(balance=50)
    
    vk.create_director(
        first_name="Владимир",
        second_name="Кириенко", 
        Id=1,
        salary=15
    )
    
    vk.create_employee(
        first_name="Елена",
        second_name="Иванова",
        Id=2,
        salary=8
    )
    
    vk.create_employee(
        first_name="Виктор", 
        second_name="Кузнецов",
        Id=3,
        salary=6
    )
    
    vk.set_profit(145.12)
    result1 = vk.fulfill_promise()
    print(f"Первая выплата: {result1}")  # True
    
    director = vk.director()
    print(f"Директор проверяет Promise: {director.check_promises()}")  # True
    
    vk.set_profit(-200)
    result2 = vk.fulfill_promise()
    print(f"Вторая выплата: {result2}")  # False
    
    print(f"Директор проверяет Promise: {director.check_promises()}")  # False
    
    # Дополнительная информация
    print(f"\nБаланс компании: {vk.balance}")
    print(f"Количество сотрудников: {len(vk.employees)}")