'''

Мини-библиотека реализующая интервалы, с функционалом их объединения,
вычисления ширины, проверки на эквивалентность.
В состав бибилиотеки должен также входить парсер,
который считывает строковое представление интеравлов
и по нему создает нужные объекты.

Примеры работы с библиотекой:

[ (0, 1), (1, 7), (7, 10] ] + {0, 1, 7} = [0, 10] (добавление точек)
[5, 6] + (-2, 4) = [(-2, 4), [5, 6]] (объединение интервалов)
(0, 12) + [ (-2, 1), (7, 10] ] = (-2, 12) (объединение интервалов в один)

'''

# mass_left_bracket = {"(", "[", "{"}
# mass_right_bracket = {")", "]", "}"}


class Interval():
    # mass_left_bracket = {"(", "[", "{"}
    # mass_right_bracket = {")", "]", "}"}
    # promezg: list
    left_bracket: str
    left_border: int
    right_border: int
    right_bracket: str

    # Инициализируем
    def __init__(self, left_bracket, left_border, right_border, right_bracket):
        self.left_bracket = left_bracket
        self.left_border = int(left_border)
        self.right_border = int(right_border)
        self.right_bracket = right_bracket

    # Выводим интервал
    def __str__(self):
        return f"{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}"


# Считываем интервал
def read_int(st: str):
    if st[0] == "[":
        left_bracket = "["
        left_border = ""
        right_border = ""
        right_bracket = "end"
        i = 1
        while st[i] != ",":
            left_border += st[i]
            i += 1
        i += 2
        while st[i] != "]":
            right_border += st[i]
            i += 1
        right_bracket = st[i]
        # tmp = left_bracket + left_border + right_border + right_bracket

        # return f"{left_bracket}{left_border}, {right_border}{right_bracket}"

        interval = Interval(left_bracket, left_border, right_border, right_bracket)
        return interval
    # Вписать этот случай в условие выше
    elif st[0] == "(":
        pass

    # Считываем точку и переводим её в интервал
    elif st[0] == "{":
        pass






def read_point(self):
    pass


# парсер, который считывает строковое представление интеравлов
def parser():
    pass


# Добавление точек
def Add(str):
    pass


# Объединение интервалов
def Merger(str):
    pass


if __name__ == "__main__":
    # inter = Interval("(","2", "4", ")")
    # print(inter)
    print(read_int("[12, 34]"))

