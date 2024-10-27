#Задача 9.1
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        return self.age >= 18

# Пример использования
person1 = Person("Ivan", "Ivanov", 16)
print(person1.full_name())


#Задача 9*
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"


laptop1 = Laptop("Apple", "MacBook Pro", 1500)
print(laptop1.laptop_name) 

