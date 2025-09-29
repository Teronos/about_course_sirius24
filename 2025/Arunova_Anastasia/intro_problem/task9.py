# Создайте класс Laptop, у которого есть:
# - Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука.
#   На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price
#   и также атрибут laptop_name — строковое значение, следующего вида: "brand model"
# - Метод laptop_name возвращающий аналогичное значение поля.

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.__laptop_name = f"{self.brand} {self.model}"

    def laptop_name(self):
        return self.__laptop_name

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name())