# Создайте класс Laptop, у которого есть:
# Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name — строковое значение, следующего вида: « brand model>»
# Метод laptop_name возврашающий аналогичное значение поля.

class Laptop:

    __brand: str
    __model: str
    price: float
    laptop_name: str

    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.price = price
        self.laptop_name = brand + " " + model

    def get_laptop_name(self) -> str:
        return self.laptop_name


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"