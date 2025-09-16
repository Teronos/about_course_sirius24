#Создайте класс Person, у которого есть:

#Конструктор, принимающий имя, фамилию и возраст. Их необходимо сохранить в поля экземпляра класса first_name, last_name, age.

#Метод full_name, который возвращает строку в виде "<Фамилия> <Имя>".

#Метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае


class Person:
  # Создаем конструктор, который принимает имя, фамилию и возраст
  def __init__(self, first_name, last_name, age) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  # Создаем метод full_name, который напечатает фамилию и имя
  def full_name(self) -> str:
    return f"{self.last_name} {self.first_name}"

  # Создаем метод is_adult, который вернет True, если человек достиг 18 лет и False в противном случае
  def is_adult(self) -> bool:
    if self.age >= 18:
      return True
    else:
      return False
	  
	
p1 = Person ('Ivan', 'Ivanov', 23)
p2 = Person ('Petr', 'Petrov', 41)
p3 = Person ('Olga', 'Sidorova', 16)

print(p1.full_name()) # Выводит Фамилию и имя объекта 1
print(p2.is_adult()) # Объект 2 старше 18, поэтому выводит True
print(p3.is_adult()) # Объект 3 младше 18, поэтому выводит False