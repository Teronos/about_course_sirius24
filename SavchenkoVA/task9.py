import math

"""
Задача 9:
Создайте класс Point. У этого класса должны быть:
* Метод set_coordinates, который принимает координаты точки на плоскости
и сохраняет их в экземпляр класса в атрибуты x и y.
* Метод get_distance, который обязательно принимает экземпляр класса Point
и возвращает расстояние между двумя точками по теореме Пифагора.
В случае, если в данный метод передается не экземпляр класса Point,
необходимо вывести сообщение "Передана не точка".
"""


class Point:
    def __init__(self):
        self.y = None
        self.x = None

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point):
        if type(point) != Point:
            print('Передана не точка')
            return None
        distance = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return distance


def task9():
    p1 = Point()
    p2 = Point()
    p1.set_coordinates(1, 2)
    p2.set_coordinates(4, 6)
    print('Разница между (' + str(p1.x) + ', ' + str(p1.y) + ') и (' + str(p2.x) + ', ' + str(p2.y) + ') равна: ', end='')
    d = p1.get_distance(p2)
    print(d)
    print('Разница между (' + str(p1.x) + ', ' + str(p1.y) + ') и 10 равна: ', end='')
    p1.get_distance(10)


"""
Задача 9.1:
Создайте класс Person, у которого есть:
* Конструктор, принимающий имя, фамилию и возраст.
Их необходимо сохранить в поля экземпляра класса first_name, last_name, age.
* Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".
* Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае.
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        return self.age >= 18


def task9_1():
    p1 = Person('Nik', 'Abaturov', 14)
    p2 = Person('Nika', 'Savchenko', 24)
    print('Персона', p1.full_name(), 'является совершеннолетней:', p1.is_adult())
    print('Персона', p2.full_name(), 'является совершеннолетней:', p2.is_adult())


"""
Задача 9*:
Создайте класс Laptop, у которого есть:
* Конструктор, принимающий 3 аргумента: бренд, модель и цену ноутбука.
На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price
и также атрибут laptop_name — строковое значение, следующего вида: «brand model»
* Метод laptop_name возвращающий аналогичное значение поля.
"""



class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self._laptop_name = brand + ' ' + model

    def laptop_name(self):
        return self._laptop_name

def task9_p():
    hp = Laptop('hp', '15-bw0xx', 57000)
    print('Результат созданного класса:')
    print('Стоимость:', hp.price)
    print('Имя компьютера:', hp.laptop_name())


if __name__ == "__main__":
    print('Задача 9:')
    task9()
    print('\nЗадача 9.1:')
    task9_1()
    print('\nЗадача 9*:')
    task9_p()
