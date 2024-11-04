# Задача 9*
# Создайте класс Laptop, у которого есть:
# Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука.
# На основании этих аргументов нужно для экземпляра создать атрибуты
# brand, model, price и также атрибут laptop_name — строковое значение,
# следующего вида: « brand model>»
# Метод laptop_name возврашающий аналогичное значение поля.
# [ ]
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name()) # выводит "hp 15-bw0xx"

class Laptop:
    def __init__(self, brand: str, model: str, price) -> 'Laptop':
        self.brand = brand
        self.model = model
        self.price = price

    def laptop_name(self) -> str:
# print(hp.laptop_name()) # выводит "hp 15-bw0xx"
        return f"{self.brand} {self.model}"


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.brand) # выводит "hp"
print(hp.price) # выводит 57000
print(hp.laptop_name()) # выводит "hp 15-bw0xx"
