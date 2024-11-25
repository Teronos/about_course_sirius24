"""
class for interval
"""
from .type_open_bracket import TypeOpenBracket
from .type_closed_bracket import TypeClosedBracket


class Interval:
    left_bracket: TypeOpenBracket
    left_border: float
    right_border: float
    right_bracket: TypeClosedBracket

    # Инициализируем
    def __init__(self, str_interval: str) -> None:
        # Обработка пустой строки
        if len(str_interval) == 0:
            raise ValueError('Вы передали пустой интервал')

        self.__parser(str_interval)

    # Парсер интервалов
    def __parser(self, interval_str: str) -> None:
        # Обработка отсутствия левой скобки
        if interval_str[0] not in [
            TypeOpenBracket.CURLY.value, TypeOpenBracket.SQUARE.value, TypeOpenBracket.ROUND.value]:
            raise ValueError('В вашем интервале не хватает открывающей скобки [, ( или {')

        # Заполнение левой скобки
        match interval_str[0]:
            case '[':
                self.left_bracket = TypeOpenBracket.SQUARE
            case '(':
                self.left_bracket = TypeOpenBracket.ROUND
            case '{':
                self.left_bracket = TypeOpenBracket.CURLY
                self.right_bracket = TypeClosedBracket.CURLY

        # Поиск левого числа
        a = ''
        i = 1
        while interval_str[i].isnumeric():
            a += interval_str[i]
            i += 1

        # Обработка отсутствия числа
        if a == '':
            raise ValueError('Вы не передали число для интервала')

        # Заполнение левого числа
        self.left_border = float(a)

        # Заполнение правого числа при точке
        if self.left_bracket == TypeOpenBracket.CURLY:
            self.right_border = self.left_border
            return

        # Поиск начала числа
        while i < len(interval_str) or not interval_str[i].isnumeric():
            i += 1

        # Обработка отсутствия правого числа
        if i == len(interval_str):
            raise ValueError('Вы не передали число для интервала')

        # Поиск второго числа
        a = ''
        while i < len(interval_str) or interval_str[i].isnumeric():
            a += interval_str[i]
            i += 1

        # Обработка отсутствия правого числа
        if a == '':
            raise ValueError('Вы не передали второе число для интервала')

        # Заполнение правого числа
        self.right_border = float(a)

        # Если левая граница больше правой
        if self.left_border > self.right_border:
            print('Неверно заданы границы интервалов')
            self.right_border, self.left_border = self.left_border, self.right_border

        # Обработка отсутствия правой скобки
        if i == len(interval_str) or interval_str[i] not in [
            TypeClosedBracket.CURLY.value, TypeClosedBracket.SQUARE.value, TypeClosedBracket.ROUND.value]:
            raise ValueError('В вашем интервале не хватает закрывающей скобки ], ) или }')

        # Заполнение левой скобки
        match interval_str[i]:
            case ']':
                self.right_bracket = TypeClosedBracket.SQUARE
            case ')':
                self.right_bracket = TypeClosedBracket.ROUND

    # Выводим интервал
    def __str__(self) -> str:
        if self.left_bracket == TypeOpenBracket.CURLY:
            return f'{self.left_bracket}{self.left_border}{self.right_bracket}'
        else:
            return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Преобразуем интервал в строку
    def __repr__(self) -> str:
        if self.left_bracket == TypeOpenBracket.CURLY:
            return f'{self.left_bracket}{self.left_border}{self.right_bracket}'
        else:
            return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Ширина интервала
    def weight(self) -> float:
        return self.right_border - self.left_border

    # Перегрузка '=='
    def __eq__(self, other) -> bool:
        # Проверка на подходящий тип интервала
        if not isinstance(other, (Interval, Intervals)):
            raise TypeError('Сравнение интервала не с интервалом не возможно')
        obj = other
        # Проверка на длину интервалса
        if isinstance(other, Intervals):
            if len(other.list_intervals) > 1:
                return False
            else:
                obj = other.list_intervals[0]
        # Проверка на равенства интервала
        if (self.left_bracket == obj.left_bracket) and (
                self.left_border == obj.left_border) and (
                self.right_border == obj.right_border) and (
                self.right_bracket == obj.right_bracket):
            return True
        else:
            return False

    # Перегрузка '<'
    def __lt__(self, other) -> bool:
        # Проверка на подходящий тип интервала
        if not isinstance(other, (Interval, Intervals)):
            raise TypeError('Сравнение интервала не с интервалом не возможно')
        obj = other
        # Проверка на длину интервалса
        if isinstance(other, Intervals):
            if len(other.list_intervals) > 1:
                return True
            else:
                obj = other.list_intervals[0]
        # Проверка на уменьшение интервала
        if self.left_border < obj.left_border:
            return True
        elif self.left_border == obj.left_border:
            if self.right_border < obj.right_border:
                return True
        return False

    # Приватная функция для сложения
    def __add(self, other):
        # Если левые границы интервалов равны
        if self.left_border == other.left_border:
            s = ''
            if self.left_bracket == other.right_bracket == TypeOpenBracket.ROUND:
                s = '('
            else:
                s = '['
            s += str(self.left_border) + ', '
            if self.right_border > other.right_border:
                s += str(self.right_border) + self.right_bracket.value
            elif self.right_border < other.right_border:
                s += str(other.right_border) + other.right_bracket.value
            else:
                s += str(other.right_border)
                if self.left_bracket == other.right_bracket == TypeOpenBracket.ROUND:
                    s += other.right_bracket.value
                else:
                    s += ']'
            if self.left_border == other.left_border == self.right_border == other.right_border:
                return [Interval('{' + str(self.left_border) + '}')]
            return [Interval(s)]
        # Есть пересечение второго интервала с первым
        if self.right_border > other.left_border:
            # Есть включение второго интервала в первый
            if self.right_border > other.right_border:
                return [self]
            return [Interval(self.left_bracket.value + str(self.left_border) + ', ' +
                             str(other.right_border) + other.right_bracket.value)]
        elif self.right_border == other.left_border:
            if self.right_bracket != TypeClosedBracket.ROUND or other.left_bracket != TypeOpenBracket.ROUND:
                if self.left_border == other.left_border == self.right_border == other.right_border:
                    return [Interval('{' + str(self.left_border) + '}')]
                return [Interval('[' + str(self.left_border) + ', ' + str(other.right_border) + ']')]
            else:
                return [self, other]
        return [self, other]

    # Сложение для интервала, интервалса и точек
    def __add__(self, other):
        # Проверка на подходящий тип интервала
        if not isinstance(other, (Interval, Intervals, int, float)):
            raise TypeError('Добавление интервала или точки не возможно')
        obj = other

        # Преобразование числа и интервался в лист интервалов
        if isinstance(other, (int, float)):
            obj = [Interval('{' + str(other) + '}')]
        elif isinstance(other, Intervals):
            obj = []
            for inter in other.list_intervals:
                obj.append(inter)

        # Добавление интервала в лист для упрощения сложения
        obj.append(self)

        # Сортировка листа по увеличению
        sorted(obj)

        # Сложение интервалов по элементно с листом
        result = [obj[0]]
        for i in range(1, len(obj)):
            res = result[-1].__add(obj[i])
            if len(res) > 1:
                result.append(obj[i])
            else:
                result[-1] = res

        # Если в листе остался один интервал, то вернуть интервал, иначе лист интервалов
        if len(result) > 1:
            return result
        return result[0]


"""
class for intervals
"""


class Intervals:
    list_intervals: list

    # list_intervals: list[Interval]

    def __init__(self):
        self.list_intervals = []
        # list_intervals = [self]
        # list_intervals.append[self]

    @classmethod
    def parser(cls, intervals_srt):
        intervals = cls()
        if intervals_srt[0] == '{':
            new_intervals_srt = intervals_srt
        else:
            new_intervals_srt = intervals_srt[1:-1]
        while len(new_intervals_srt) > 1:
            i = 0
            while new_intervals_srt[i] != ']' and new_intervals_srt[i] != ')' and new_intervals_srt[i] != '}':
                i += 1
            part = new_intervals_srt[:i + 1]
            # Обработка массива точек
            if part[0] == '{' and ',' in part:
                new_points = part[1:-1]
                array_points = new_points.split(', ')
                for point in array_points:
                    inter = Interval.parser('{' + point + '}')
                    intervals.list_intervals.append(inter)
            else:
                inter = Interval.parser(part)
                intervals.list_intervals.append(inter)
            if len(new_intervals_srt[i + 1:]) > 3:
                new_intervals_srt = new_intervals_srt[i + 3:]
            else:
                new_intervals_srt = new_intervals_srt[i + 1:]

        return intervals

    # TODO - подумать как оно должно работать (это довавление а не сумма)
    def __add__(self, other):
        intervals = Intervals()
        for inter1 in self.list_intervals:
            intervals.list_intervals.append(inter1)
        for inter2 in other.list_intervals:
            intervals.list_intervals.append(inter2)
        return intervals.union()

    def union(self):
        intervals = Intervals()
        # Сортировка
        self.list_intervals.sort()
        first_inter = self.list_intervals[0]
        intervals.list_intervals.append(first_inter)
        for inter_old in self.list_intervals[1:]:
            summ = inter_old + intervals.list_intervals[-1]
            if isinstance(summ, Interval):
                intervals.list_intervals[-1] = summ
            else:
                intervals.list_intervals.append(inter_old)
        return intervals

    def __str__(self):
        output_inter = '['
        for inter in self.list_intervals:
            output_inter += inter.__repr__() + ', '

        output_inter = output_inter[:-2]
        output_inter += ']'
        return output_inter

    def __repr__(self):
        output_inter = '['
        for inter in self.list_intervals:
            output_inter += inter.__repr__() + ', '

        output_inter = output_inter[:-2]
        output_inter += ']'
        return output_inter

    def weight(self):
        sum_weight = 0
        for interv in self.list_intervals:
            sum_weight += interv.weight()
        return sum_weight

    # эквивалентность
    def equivalence(self, other):
        result = False
        self = self.union()
        other = other.union()
        if (len(self.list_intervals) == len(other.list_intervals)) and (self.weight() == other.weight()):
            for i in range(len(self.list_intervals)):
                if self.list_intervals[i] != other.list_intervals[i]:
                    return False
                else:
                    result = True
        return result


class Intervals():
    list_intervals: list

    # list_intervals: list[Interval]

    def __init__(self):
        self.list_intervals = []
        # list_intervals = [self]
        # list_intervals.append[self]

    @classmethod
    def parser(cls, intervals_srt):
        intervals = cls()
        if intervals_srt[0] == '{':
            new_intervals_srt = intervals_srt
        else:
            new_intervals_srt = intervals_srt[1:-1]
        while len(new_intervals_srt) > 1:
            i = 0
            while new_intervals_srt[i] != ']' and new_intervals_srt[i] != ')' and new_intervals_srt[i] != '}':
                i += 1
            part = new_intervals_srt[:i + 1]
            # Обработка массива точек
            if part[0] == '{' and ',' in part:
                new_points = part[1:-1]
                array_points = new_points.split(', ')
                for point in array_points:
                    inter = Interval.parser('{' + point + '}')
                    intervals.list_intervals.append(inter)
            else:
                inter = Interval.parser(part)
                intervals.list_intervals.append(inter)
            if len(new_intervals_srt[i + 1:]) > 3:
                new_intervals_srt = new_intervals_srt[i + 3:]
            else:
                new_intervals_srt = new_intervals_srt[i + 1:]

        return intervals

    # TODO - подумать как оно должно работать (это довавление а не сумма)
    def __add__(self, other):
        intervals = Intervals()
        for inter1 in self.list_intervals:
            intervals.list_intervals.append(inter1)
        for inter2 in other.list_intervals:
            intervals.list_intervals.append(inter2)
        return intervals.union()

    def union(self):
        intervals = Intervals()
        # Сортировка
        self.list_intervals.sort()
        first_inter = self.list_intervals[0]
        intervals.list_intervals.append(first_inter)
        for inter_old in self.list_intervals[1:]:
            summ = inter_old + intervals.list_intervals[-1]
            if isinstance(summ, Interval):
                intervals.list_intervals[-1] = summ
            else:
                intervals.list_intervals.append(inter_old)
        return intervals

    def __str__(self):
        output_inter = '['
        for inter in self.list_intervals:
            output_inter += inter.__repr__() + ', '

        output_inter = output_inter[:-2]
        output_inter += ']'
        return output_inter

    def __repr__(self):
        output_inter = '['
        for inter in self.list_intervals:
            output_inter += inter.__repr__() + ', '

        output_inter = output_inter[:-2]
        output_inter += ']'
        return output_inter

    def weight(self):
        sum_weight = 0
        for interv in self.list_intervals:
            sum_weight += interv.weight()
        return sum_weight

    # эквивалентность
    def equivalence(self, other):
        result = False
        self = self.union()
        other = other.union()
        if (len(self.list_intervals) == len(other.list_intervals)) and (self.weight() == other.weight()):
            for i in range(len(self.list_intervals)):
                if self.list_intervals[i] != other.list_intervals[i]:
                    return False
                else:
                    result = True
        return result