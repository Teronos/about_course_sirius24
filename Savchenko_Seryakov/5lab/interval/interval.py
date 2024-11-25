"""
class for interval
"""
from .type_open_bracket import TypeOpenBracket
from .type_closed_bracket import TypeClosedBracket


class Interval:
    left_bracket: str
    left_border: int
    right_border: int
    right_bracket: str

    # Инициализируем
    def __init__(self, left_bracket, left_border, right_border, right_bracket):
        # def __init__(self, input_interval: str):
        # TODO: подумать над проверкой скобок подходящих в enum
        """
        if not isinstance(left_bracket, TypeOpenBracket) or not isinstance(right_bracket, TypeClosedBracket):
            raise ValueError('Левые и правые границы должны быть экземплярами Type_Bracket.')
        """

        # Код от чата:
        # TODO Проверяем, что переданы корректные скобки
        """
        if left_bracket not in {b.value for b in TypeOpenBracket}:
            raise ValueError(f"Некорректная левая скобка: {left_bracket}")
        if right_bracket not in {b.value for b in TypeClosedBracket}:
            raise ValueError(f"Некорректная правая скобка: {right_bracket}")
        """

        self.left_bracket = str(left_bracket)
        self.left_border = int(left_border)
        self.right_border = int(right_border)
        self.right_bracket = str(right_bracket)

        # Если левая граница больше правой
        if self.left_border > self.right_border:
            # raise ValueError('Неверно заданы границы интервалов')
            print('Неверно заданы границы интервалов')

    #
    # Декоратор для создания методов класса
    # Используем для создания объектов (Для альтернативного способа инициализации)
    #
    # Парсер интервалов
    @classmethod
    def parser(cls, interval_str: str):
        # Считываем интервал
        if interval_str[0] == '[' or interval_str[0] == '(':
            left_bracket = interval_str[0]
            left_border = ''
            right_border = ''
            i = 1
            while interval_str[i] != ',':
                left_border += interval_str[i]
                i += 1
            i += 2
            while interval_str[i] != ']' and interval_str[i] != ')':
                right_border += interval_str[i]
                i += 1
            right_bracket = interval_str[i]

        # Считываем точку и переводим её в интервал
        elif interval_str[0] == '{':
            left_bracket = '['
            left_border = ''
            right_border = ''
            i = 1
            while interval_str[i] != '}':
                left_border += interval_str[i]
                i += 1
            right_border = left_border
            right_bracket = ']'
        return cls(left_bracket, left_border, right_border, right_bracket)

    # Выводим интервал
    def __str__(self) -> str:
        if self.left_border == self.right_border and self.left_bracket == '[' and self.right_bracket == ']':
            return f'{TypeOpenBracket.CURLY.value}{self.left_border}{TypeClosedBracket.CURLY.value}'
        else:
            return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Преобразуем интервал в строку
    def __repr__(self) -> str:
        if self.left_border == self.right_border and self.left_bracket == '[' and self.right_bracket == ']':
            return f'{TypeOpenBracket.CURLY.value}{self.left_border}{TypeClosedBracket.CURLY.value}'
        else:
            return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Ширина интервала
    def weight(self):
        return self.right_border - self.left_border

    # Пока для []
    def __add__(self, other):
        # Берём тот интервал, у которого левая граница меньше
        if self.left_border > other.left_border:
            self, other = other, self

        # Есть пересечение второго интервала с первым
        if self.right_border > other.left_border:
            # Есть включение второго интервала в первый
            if self.right_border > other.right_border:
                return self
            return Interval(self.left_bracket, self.left_border, other.right_border, other.right_bracket)

        elif self.right_border == other.left_border:
            # if self.right_bracket == TypeClosedBracket.SQUARE or other.left_bracket == TypeOpenBracket.SQUARE:
            if self.right_bracket == ']' or other.left_bracket == '[':
                return Interval(self.left_bracket, self.left_border, other.right_border, other.right_bracket)
            else:
                # return [self, other]
                intervals = Intervals()
                intervals.__add__(self)
                intervals.__add__(other)
                return intervals

        # return [self, other]
        intervals = Intervals()
        intervals.__add__(self)
        intervals.__add__(other)
        return intervals
