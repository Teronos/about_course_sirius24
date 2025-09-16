
class Person:
    first_name: str
    last_name: str
    age: int


    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age



    def full_name(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    

    def is_adult(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False



p1 = Person("oleg", "volkov", 20)
print(p1.full_name())
print(p1.is_adult())

