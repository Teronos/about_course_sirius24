"""

Мини-библиотека реализующая интервалы, с функционалом их объединения,
вычисления ширины, проверки на эквивалентность.
В состав бибилиотеки должен также входить парсер,
который считывает строковое представление интеравлов
и по нему создает нужные объекты.

Примеры работы с библиотекой:

[ (0, 1), (1, 7), (7, 10] ] + {0, 1, 7} = [0, 10] (добавление точек)
[5, 6] + (-2, 4) = [(-2, 4), [5, 6]] (объединение интервалов)
(0, 12) + [ (-2, 1), (7, 10] ] = (-2, 12) (объединение интервалов в один)

"""

from enum import Enum


class TypeOpenBracket(Enum):
    ROUND = '('
    SQUARE = '['
    CURLY_OPEN = '{'


class TypeClosedBracket(Enum):
    ROUND = ')'
    SQUARE = ']'
    CURLY_OPEN = '}'


class Interval():
    left_bracket: str
    left_border: int
    right_border: int
    right_bracket: str

    # Инициализируем
    def __init__(self, left_bracket, left_border, right_border, right_bracket):
        # TODO: подумать над проверкой скобок подходящих в enum
        """
        if not isinstance(left_bracket, TypeOpenBracket) or not isinstance(right_bracket, TypeClosedBracket):
            raise ValueError('Левые и правые границы должны быть экземплярами Type_Bracket.')
        """
        self.left_bracket = str(left_bracket)
        self.left_border = int(left_border)
        self.right_border = int(right_border)
        self.right_bracket = str(right_bracket)
        # Если левая граница больше правой
        if self.left_border > self.right_border:
            # raise ValueError('Неверно заданы границы интервалов')
            print('Неверно заданы границы интервалов')

    # Выводим интервал
    def __str__(self) -> None:
        return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Преобразуем интервал в строку
    def __repr__(self) -> None:
        return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    def __add__(self):
        pass

    # Ширина интервала
    def weight(self):
        return self.right_border - self.left_border


# Считываем интервал
def read_int(st: str):
    if st[0] == '[' or st[0] == '(':
        left_bracket = st[0]
        left_border = ''
        right_border = ''
        i = 1
        while st[i] != ',':
            left_border += st[i]
            i += 1
        i += 2
        while st[i] != ']' and st[i] != ')':
            right_border += st[i]
            i += 1
        right_bracket = st[i]
        interval = Interval(left_bracket, left_border, right_border, right_bracket)
        return interval

    # Считываем точку и переводим её в интервал
    elif st[0] == '{':
        left_bracket = '['
        left_border = ''
        right_border = ''
        i = 1
        while st[i] != '}':
            left_border += st[i]
            i += 1
        right_border = left_border
        right_bracket = ']'
        interval = Interval(left_bracket, left_border, right_border, right_bracket)
        return interval


# Добавление точек
def Add(str):
    pass


# Объединение интервалов
def Merger(str):
    pass


if __name__ == '__main__':
    inter = Interval('(', '2', '4', ')')
    print(inter)
    print(inter.weight())
    print(read_int('[52, 34]'))
    print(read_int('[-123, 3)'))
    print(read_int('{-123}'))
