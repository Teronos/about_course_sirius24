#Создайте класс Point. У этого класса должны быть:

#Метод set_coordinates, который принимает координаты точки на плоскости и сохраняет их в экземпляр класса в атрибуты x и y.

#Метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора. 
#В случае, если в данный метод передается не экземпляр класса Point, необходимо вывести сообщение "Передана не точка".

class Point:
  # Создаем метод set_coordinates, который принимает координаты и сохраняет в атрибуты х и у
    def set_coordinates(self, x, y) -> None:
        self.x = x
        self.y = y

  # Создаем метод get_distance, который выводит расстояние между двумя точками
    def get_distance(self, p) -> float:
      if isinstance(p, Point):
          return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5
      else:
        print("Передана не точка")

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)

d = p1.get_distance(p2) # вернёт 5.0
print(d)

p1.get_distance(10) # Распечатает "Передана не точка"