# Задание 2*
# Дано шестизначное число. Найдите суммы его четных и нечетных элементов. Образуйте из них этих сумм одно число и выведите его на экран

class Task2:

    @staticmethod
    def sum_digits_of_number(number):
        even_digits_sum = 0
        odd_digits_sum = 0

        if number == "0":
            return "0"

        if number == "" or number[0] == "0":
            print("Ошибка ввода данных")
            return None

        for digit in number:
            try:
                if number.index(digit) % 2 == 0:
                    even_digits_sum += int(digit)
                else:
                    odd_digits_sum += int(digit)
            except ValueError:
                print("Ошибка ввода данных")
                return None
        return f"{even_digits_sum}{odd_digits_sum}"


if __name__ == '__main__':
    number = input("Введите число: ")
    print(Task2.sum_digits_of_number(number))
