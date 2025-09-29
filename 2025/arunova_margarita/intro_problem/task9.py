"""
Создайте класс Laptop, у которого есть:

* Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука.
  На основании этих аргументов нужно для экземпляра создать атрибуты
  brand, model, price и также атрибут laptop_name — строковое значение, следующего вида: «brand model»
* Метод laptop_name возврашающий аналогичное значение поля.
"""

class Laptop:
    def __init__(self, brand: str, model: str, price: float) -> None:
        self.brand: str = brand
        self.model: str = model
        self.price: float = price
        self.__laptop_name: str = f"{self.brand} {self.model}"

    def laptop_name(self) -> str:
        return self.__laptop_name

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # 57000
print(hp.laptop_name()) # "hp 15-bw0xx"