# Задание 1*
# Дано пятизначное число. Найдите произведение его цифр.
class Task1:

    @staticmethod
    def multiply_digits_of_number(num):
        res = 1

        if len(num) > 1 and num[0] == "0" or num == "":
            print("Ошибка ввода данных")
            return None

        for digit in num:
            try:
                res = res * int(digit)
            except ValueError:
                print("Ошибка ввода данных")
                return None
        return res


if __name__ == '__main__':
    number = input("Введите число: ")
    print(Task1.multiply_digits_of_number(number))