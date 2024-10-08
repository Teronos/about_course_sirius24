from enum import Enum
from typing import List

# Перечисление ролей пользователей
class Role(Enum):
    Admin = 1
    Teacher = 2
    Student = 3

# Класс для представления домашнего задания
class Homework:
    def __init__(self, title: str, description: str, deadline: str):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.tasklist: List[str] = []  # Список задач по домашнему заданию

    def add_task(self, task: str):
        """Добавить задачу в список задач"""
        self.tasklist.append(task)

    def __repr__(self):
        return f"Homework(title={self.title}, deadline={self.deadline})"

# Класс для представления пользователя системы
class User:
    def __init__(self, last_name: str, first_name: str, login: str, password_hash: str, role: Role):
        self.last_name = last_name
        self.first_name = first_name
        self.login = login
        self.__password_hash = password_hash
        self.__role = role
        self.homeworks: List[Homework] = []  # Домашние задания для студентов

    def is_admin(self) -> bool:
        """Проверка, является ли пользователь администратором"""
        return self.__role == Role.Admin

    def is_teacher(self) -> bool:
        """Проверка, является ли пользователь преподавателем"""
        return self.__role == Role.Teacher

    def is_student(self) -> bool:
        """Проверка, является ли пользователь студентом"""
        return self.__role == Role.Student

    def add_homework(self, homework: Homework):
        """Добавить домашнее задание пользователю (для студентов)"""
        if self.is_student():
            self.homeworks.append(homework)
        else:
            raise PermissionError("Только студенты могут получать домашние задания.")

    def __repr__(self):
        return f"User(login={self.login}, role={self.__role.name})"

# Класс для представления учебной группы
class Group:
    def __init__(self, group_id: int, teacher: User):
        self.group_id = group_id
        self.teacher = teacher
        self.students: List[User] = []  # Студенты группы
        self.homeworks: List[Homework] = []  # Домашние задания для группы

    def add_student(self, student: User):
        """Добавить студента в учебную группу"""
        if student.is_student():
            self.students.append(student)
        else:
            raise ValueError("Только студенты могут быть добавлены в группу.")

    def assign_homework(self, homework: Homework):
        """Назначить домашнее задание всей группе"""
        if self.teacher.is_teacher():
            self.homeworks.append(homework)
            for student in self.students:
                student.add_homework(homework)
        else:
            raise PermissionError("Только преподаватель может назначать домашние задания.")

    def __repr__(self):
        return f"Group(ID={self.group_id}, teacher={self.teacher.first_name} {self.teacher.last_name})"





# Создаем пользователей
admin = User('Ivanov', 'Ivan', 'admin_ivanov', 'hashed_pass_1', Role.Admin)
teacher = User('Petrov', 'Petr', 'teacher_petrov', 'hashed_pass_2', Role.Teacher)
student1 = User('Sidorov', 'Sergey', 'student_sidorov', 'hashed_pass_3', Role.Student)
student2 = User('Smirnov', 'Alexey', 'student_smirnov', 'hashed_pass_4', Role.Student)

# Создаем группу и добавляем студентов
group1 = Group(1, teacher)
group1.add_student(student1)
group1.add_student(student2)

# Создаем домашнее задание
homework1 = Homework('Math Homework', 'Solve 10 equations', '2024-10-10')
homework1.add_task('Solve equation 1')
homework1.add_task('Solve equation 2')

# Назначаем домашнее задание группе
group1.assign_homework(homework1)

# Проверка домашних заданий у студентов
print(student1.homeworks) 
print(student2.homeworks) 
