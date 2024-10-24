#Задание 1

number = int(input("Введите трёхзначное число: "))


sum = number // 100 + (number // 10 % 10) + (number % 10)

print("Результат:", sum)

#Задание 1*


number = int(input("Введите пятизначное число: "))


sum_1 = (number // 10000) * (number // 1000 % 10) * (number // 100 % 10) * (number // 10 % 10) * (number % 10)


print("Результат:", sum_1)

#Задание 2
n_1 = input("Введите трехзначное число: ")
n_list = list(n_1)
n_list.reverse()
n_2 = "".join(n_list)
print('"Результат:', n_2)

#Задание 2*
n = input("Введите шестизначное число: ")

even = 0
odd = 0

for i in n:
    i_1 = int(i)
    if int(i) % 2 == 0:
        even += i_1
    else:
        odd += i_1

print("Сумма четных: %d, сумма нечетных: %d" % (even, odd))

#Задание 3
123
n = int(input("Введите количество чисел N: "))

zero_n = 0

for _ in range(n):
    number = int(input())
    if number == 0:
        zero_n += 1

print("Количество нулей:", zero_n)

#Задание 3*
N = int(input("Введите количество чисел N: "))

sum_N_3 = 0
count_N_3 = 0


for _ in range(N):
    number = int(input())
    if number % 3 == 0:
        sum_N_3 += number
        count_N_3 += 1

if count_N_3 > 0:
    average = sum_N_3 / count_N_3
    print("Среднее арифметическое чисел:", average)
else:
    print(-1)

#Задание 4

N = int(input("Введите количество чисел N: "))

min_N = int(input())
count_min_N = 1

for _ in range(N - 1):
    number = int(input())

    if number < min_N:
        min_N = number
        count_min_N = 1
    elif number == min_N:
        count_min_N += 1

print("Количество минимальных элементов:", count_min_N)

# Задание 4*
f = 0
f_1 = 1
f_2 = 0
i = 0
a = int(input("Введите число Фибоначчи"))
while f <= a:
     f = f_1 + f_2
     f_1, f_2 = f, f_1
     i += 1
if a == f_2:
     print(i)
else:
     print(-1)

# Задание 5

def largest_multiple_of_7(a, b):

     largest = b - (b % 7)

     if largest >= a:
          return largest
     else:
          return -1

result = largest_multiple_of_7(int(input()), int(input()))
print(result)

#Задание 5.1

def complement_dna(dna_sequence):

     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
     complementary_sequence = ''.join([complement[base] for base in dna_sequence])

     return complementary_sequence

result = complement_dna(input())
print(result)

# #Задание 5*
def powers_of_two(n):
    power = 1
    result = []

    while power <= n:
        result.append(power)
        power *= 2

    return result

result = map(str,powers_of_two(int(input())))
print(' '.join(result))

# #Задание 6
def find_maximum(n):
    numbers = []

    for _ in range(n):
        number = int(input())
        numbers.append(number)

    maximum = max(numbers)
    return maximum

n = int(input("Введите количество чисел: "))
result = find_maximum(n)
print(result)

##Задание 6*
def count_positive_numbers(n):
    count = 0

    for _ in range(n):
        number = int(input())
        if number > 0:
            count += 1

    return count

n = int(input("Введите длину последовательности N: "))
result = count_positive_numbers(n)
print(result)

#Задача 7
def sum_two_digit_multiples_of_eight(n, numbers):
    total_sum = 0

    for number in numbers:
        if 10 <= number <= 99 and number % 8 == 0:
            total_sum += number

    return total_sum

n = int(input("Введите количество чисел n: "))
numbers = list(map(int, input("Введите n чисел: ").split()))

result = sum_two_digit_multiples_of_eight(n, numbers)
print(result)

#Задача 7*
def count_max_elements():
    numbers = []

    while True:
        number = int(input())
        if number == 0:
            break
        numbers.append(number)

    if not numbers:
        return 0

    max_number = max(numbers)
    count = numbers.count(max_number)

    return count

result = count_max_elements()
print(result)

#Задание 8
def common_digits(num1, num2):

    str_num1 = str(num1)
    str_num2 = str(num2)

    result = []

    for digit in str_num1:

        if digit in str_num2 and digit not in result:
            result.append(digit)

    print(' '.join(result))

common_digits(int(input()), int(input()))

#Задание 8*

def my_sort(array):
    result = []
    while array:

        result += array.pop(0)

        if array and array[0]:
            for row in array:
                result.append(row.pop())

        if array:
            result += array.pop()[::-1]


        if array and array[0]:
            for row in reversed(array):
                result.append(row.pop(0))

    return result


def user_input_array():

    n = int(input("Введите размер массива n (матрица будет n x n): "))

    array = []
    for i in range(n):

        row = list(map(int, input(f"Введите элементы {i + 1}-й строки, разделенные пробелом: ").split()))
        if len(row) != n:
            print(f"Ошибка: строка должна содержать ровно {n} элементов!")
            return None
        array.append(row)

    return array


array = user_input_array()
if array:
    sorted_elements = my_sort(array)
    print("Результат сортировки по часовой стрелке:", sorted_elements)

#Задание 9.1

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        return self.age >= 18


person = Person("Иван", "Петров", 20)

print(person.full_name())
print(person.is_adult())

#Задание 9*
class Laptop:
    def __init__(self, brand, model, price):

        self.brand = brand
        self.model = model
        self.price = price

        self.laptop_name = f"{self.brand} {self.model}"

    def get_laptop_name(self):
        return self.laptop_name


laptop = Laptop("Dell", "XPS 13", 1200)
print(laptop.get_laptop_name())
print(laptop.price)

# Задание  10*
class Promise:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary
        self.paid = False

    def fulfill(self):
        self.paid = True

    def reset(self):
        self.paid = False


class Employee:
    def __init__(self, first_name, second_name, Id, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.Id = Id
        self.promise = Promise(Id, salary)


class Director(Employee):
    def __init__(self, first_name, second_name, Id, salary):
        super().__init__(first_name, second_name, Id, salary)
        self.company = None

    def check_promises(self):
        if self.company:
            return all(promise.paid for promise in self.company.promises.values())
        return False


class Company:
    def __init__(self, balance=0):
        self.balance = balance
        self._director = None
        self.employees = []
        self.promises = {}

    def create_director(self, first_name, second_name, Id, salary):
        if self._director is not None:
            raise ValueError("Компания уже имеет директора.")
        self._director = Director(first_name, second_name, Id, salary)
        self._director.company = self

        self.add_employee(self._director)

    def create_employee(self, first_name, second_name, Id, salary):
        employee = Employee(first_name, second_name, Id, salary)
        self.add_employee(employee)

    def add_employee(self, employee):
        self.employees.append(employee)

        self.promises[employee.Id] = employee.promise

    def set_profit(self, amount):
        self.balance += amount

    def fulfill_promise(self):
        total_salary = sum(promise.salary for promise in self.promises.values())

        if self.balance >= total_salary:
            for promise in self.promises.values():
                promise.fulfill()
            self.balance -= total_salary
            return True
        else:
            for promise in self.promises.values():
                promise.reset()
            return False

    def director(self):
        return self._director

vk = Company(balance=50)
vk.create_director(
  first_name = "Владимир",
  second_name = "Кириенко",
  Id = 1,
  salary = 15
  )

vk.create_employee(
  first_name = "Елена",
  second_name = "Иванова",
  Id = 2,
  salary = 8
)

vk.create_employee(
  first_name = "Виктор",
  second_name = "Кузнецов",
  Id = 3,
  salary = 6
)

vk.set_profit(145.12)
print(vk.balance)
print(vk.fulfill_promise())

director = vk.director()

print(director.check_promises())

vk.set_profit(-200)

print(vk.balance)

print(vk.fulfill_promise())
print(director.check_promises())