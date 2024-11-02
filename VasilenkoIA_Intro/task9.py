#Задача 9*
#Создайте класс Laptop, у которого есть:
#Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name — строковое значение, следующего вида: « brand model>»
#Метод laptop_name возврашающий аналогичное значение поля.

class Laptop:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand: str = brand
        self.model: str = model
        self.price: float = price
        self.laptop_name: str = f"{self.brand} {self.model}"

    def laptop_name(self) -> str:
        return self.laptop_name

#Проверка

laptop = Laptop("Apple", "MacBook Pro", 200000)
print(laptop.laptop_name)