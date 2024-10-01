import math

class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)
    
    def get_distance(self, other_point):
        if isinstance(other_point, Point):
            # по формуле Пифагора
            distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
            return distance
        else:
            # Сообщение, если передан не экземпляр класса Point
            print("Передана не точка")




p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(3, 4)

d = p1.get_distance(p2)  
print(d)

