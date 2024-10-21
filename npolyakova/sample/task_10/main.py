from sample.task_10.company import Company
from sample.task_10.director import Director
from sample.task_10.employee import Employee

if __name__ == '__main__':
    # инициализация компании и персонала
    company = Company("OOO Sharashkina kontora", 200)

    employee1 = Director(123, "Vasya", "Pupkin", 120.5)
    employee2 = Employee(124, "Kolya", "Zaycev", 100.0)
    employee3 = Employee(125, "Egor", "Egorov", 90.75)

    company.set_director(employee1)
    company.add_employee(employee2)
    company.add_employee(employee3)

    company.show_info()
    company.show_employees()
    print()

    months = int(input("How many months your company will work? "))

    # начинаем зарабатывать деньги заданное кол-во месяцев
    while months > 0:
        company.collect_profit()
        company.fulfill_promise()
        months -= 1

    company.get_profit()
