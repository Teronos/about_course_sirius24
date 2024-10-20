#Нужно описать структуры для платформы электронного обучения.
#В ней есть администраторы системы, преподаватели курсов и студенты, а также группы учебные и домашние задания.

from enum import Enum
class Role(Enum):
  Admin = 1
  Teacher = 2
  Student = 3

class Homework:
  Tasklist : list[str]

class User:
  __role : Role
  last_name : str
  first_name : str
  login : str
  __password_hash : int
  Homeworks : list[Homework] = []
  def __init__(self, last_name, first_name, login, password, role):
    self.last_name = last_name
    self.first_name = first_name
    self.login = login
    self.__password_hash = password
    self.__role = role

  def is_admin(self) -> bool:
      return self.__role == Role.Admin

  def is_teacher(self) -> bool:
      return self.__role == Role.Teacher


class Group:
  ID : int
  members : list[User]


