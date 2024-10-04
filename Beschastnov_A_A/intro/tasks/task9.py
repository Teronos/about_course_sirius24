import math

# 9
# Создайте класс Point. У этого класса должны быть:
#
# Метод set_coordinates, который принимает координаты точки на плоскости и сохраняет их в экземпляр
# класса в атрибуты x и y.
#
# Метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние
# между двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр
# класса Point, необходимо вывести сообщение "Передана не точка".
class Point:
    def set_coordinates(self, x: float, y: float) -> 'Point':
        self.x = x
        self.y = y

        return self

    def get_distance(self, other_point: 'Point') -> float:
        if isinstance(other_point, Point):
            return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        else:
            print("Передана не точка")

# 9.1
# Создайте класс Person, у которого есть:
#
# Конструктор, принимающий имя, фамилию и возраст. Их необходимо сохранить в поля экземпляра
# класса first_name, last_name, age.
#
# Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".
#
# Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.
class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> 'Person':
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def is_adult(self) -> bool:
        return self.age >= 18

# 9*
# Создайте класс Laptop, у которого есть:
#
# Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name — строковое значение, следующего вида: « brand model>»
# Метод laptop_name возврашающий аналогичное значение поля.
class Laptop:
    def __init__(self, brand: str, model: str, price) -> 'Laptop':
        self.brand = brand
        self.model = model
        self.price = price

    def laptop_name(self) -> str:
        return f"{self.brand} {self.model}"