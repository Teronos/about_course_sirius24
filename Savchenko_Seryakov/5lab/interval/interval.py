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
        while i < len(interval_str) and not interval_str[i].isnumeric():
            i += 1

        # Обработка отсутствия правого числа
        if i == len(interval_str):
            raise ValueError('Вы не передали число для интервала')

        # Поиск второго числа
        a = ''
        while i < len(interval_str) and interval_str[i].isnumeric():
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
            if self.left_border.is_integer():
                return f'{self.left_bracket}{int(self.left_border)}{self.right_bracket}'
            return f'{self.left_bracket}{self.left_border}{self.right_bracket}'
        else:
            if self.left_border.is_integer() and self.right_border.is_integer():
                return f'{self.left_bracket}{int(self.left_border)}, {int(self.right_border)}{self.right_bracket}'
            elif self.left_border.is_integer() and not self.right_border.is_integer():
                return f'{self.left_bracket}{int(self.left_border)}, {self.right_border}{self.right_bracket}'
            elif not self.left_border.is_integer() and self.right_border.is_integer():
                return f'{self.left_bracket}{self.left_border}, {int(self.right_border)}{self.right_bracket}'
            return f'{self.left_bracket}{self.left_border}, {self.right_border}{self.right_bracket}'

    # Преобразуем интервал в строку
    def __repr__(self) -> str:
        return self.__str__()

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

        # Преобразование числа и интервалса в лист интервалов
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

        # Сложение интервалов поэлементно с листом
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

    # Проверка на вхождение в интервал
    def __contains__(self, item) -> bool:
        # Проверка на подходящий тип интервала
        if not isinstance(item, (Interval, Intervals, int, float)):
            raise TypeError('Сравнение интервала не с интервалом не возможно')
        if isinstance(item, Intervals):
            return False
        if isinstance(item, (int, float)):
            match self.left_bracket, self.right_bracket:
                case TypeOpenBracket.SQUARE, TypeClosedBracket.SQUARE:
                    return self.left_border <= item <= self.right_border
                case TypeOpenBracket.SQUARE, TypeClosedBracket.ROUND:
                    return self.left_border <= item < self.right_border
                case TypeOpenBracket.ROUND, TypeClosedBracket.SQUARE:
                    return self.left_border < item <= self.right_border
                case TypeOpenBracket.ROUND, TypeClosedBracket.ROUND:
                    return self.left_border < item < self.right_border
                case TypeOpenBracket.CURLY, TypeClosedBracket.CURLY:
                    return self.left_border == item == self.right_border
        if item.left_border < self.left_border:
            return False
        elif item.left_border == self.left_border:
            if self.left_bracket == TypeOpenBracket.SQUARE or (
                    self.left_bracket == TypeOpenBracket.ROUND and item.left_bracket == TypeOpenBracket.ROUND):
                if item.right_border == self.right_border:
                    return self.right_bracket == TypeClosedBracket.SQUARE or (
                            self.right_bracket == TypeClosedBracket.ROUND and (
                            item.right_bracket == TypeClosedBracket.ROUND))
                else:
                    return self.right_border > item.right_border
            return False
        else:
            if self.right_border < item.left_border:
                return False
            elif self.right_border > item.right_border:
                return True
            elif self.right_border == item.right_border:
                return self.right_bracket == TypeClosedBracket.SQUARE or (
                        self.right_bracket == TypeClosedBracket.ROUND and (
                        item.right_bracket == TypeClosedBracket.ROUND))
            else:
                return False


"""
class for intervals
"""


class Intervals:
    list_intervals: list[Interval]

    # Инициализация
    def __init__(self, interval_str: str) -> None:
        self.list_intervals = []
        # Обработка пустой строки
        if len(interval_str) > 2:
            raise ValueError('Вы передали пустой список интервалов')
        self.__parser(interval_str)

    # Парсер строки в интервалс
    def __parser(self, intervals_srt: str) -> None:
        new_intervals_srt = ''
        # Предобработка входной строки
        if intervals_srt[0] == TypeOpenBracket.CURLY.value:
            new_intervals_srt = intervals_srt
        else:
            if intervals_srt[1].isnumeric():
                new_intervals_srt = intervals_srt
            else:
                new_intervals_srt = intervals_srt[1:]
            if not intervals_srt[-2].isnumeric():
                new_intervals_srt = new_intervals_srt[:-1]

        # Обработка строки
        while len(new_intervals_srt) > 1:
            i = 0
            while i < len(new_intervals_srt) and new_intervals_srt[i] not in [
                TypeClosedBracket.CURLY.value, TypeClosedBracket.ROUND.value, TypeClosedBracket.SQUARE.value]:
                i += 1
            if new_intervals_srt[i] not in [TypeClosedBracket.CURLY.value,
                                            TypeClosedBracket.ROUND.value, TypeClosedBracket.SQUARE.value]:
                raise ValueError('Вы забыли закрывающую скобку ), ] или }')
            part = new_intervals_srt[:i + 1]

            # Обработка массива точек
            if part[0] == TypeOpenBracket.CURLY.value:
                j = 1
                while j < len(part) - 1:
                    s = ''
                    while not part[j].isnumeric():
                        s += part[j]
                        j += 1
                    self.list_intervals.append(Interval('{' + s + '}'))
                    while part[j].isnumeric():
                        j += 1
            else:
                self.list_intervals.append(Interval(part))

            # Поиск начала следующего интервала
            while i < len(new_intervals_srt) and new_intervals_srt[i] not in [
                TypeOpenBracket.CURLY.value, TypeOpenBracket.ROUND.value, TypeOpenBracket.SQUARE.value]:
                i += 1
            new_intervals_srt = new_intervals_srt[i:]

    # Перегрузка +
    def __add__(self, other):
        # Проверка на подходящий тип интервала
        if not isinstance(other, (Interval, Intervals, int, float)):
            raise TypeError('Добавление интервала или точки не возможно')
        obj = other

        # Преобразование числа и интервалса в лист интервалов
        if isinstance(other, (int, float)):
            obj = [Interval('{' + str(other) + '}')]
        elif isinstance(other, Intervals):
            obj = []
            for inter in other.list_intervals:
                obj.append(inter)

        # Добавление интервалса в лист для упрощения сложения
        for inter in self.list_intervals:
            obj.append(inter)

        # Сортировка листа по увеличению
        sorted(obj)

        # Упрощение листа интервалов
        return obj.union()

    # Объединение интервалов в листе
    def union(self):
        intervals = []
        # Сортировка
        sorted(self.list_intervals)
        intervals.append(self.list_intervals[0])
        for inter_old in self.list_intervals[1:]:
            summ = inter_old + intervals[-1]
            if isinstance(summ, list):
                intervals[-1] = summ
            else:
                intervals.append(inter_old)
        self.list_intervals = intervals
        return self

    # Преобразование в строку
    def __str__(self):
        output_inter = self.list_intervals[0].__repr__()
        for i in range(1, len(self.list_intervals)):
            output_inter += ', ' + self.list_intervals[i].__repr__()
        return '[' + output_inter + ']'

    # Преобразование в строку
    def __repr__(self):
        return self.__str__()

    # Вычисление ширины
    def weight(self):
        sum_weight = 0
        for inter in self.list_intervals:
            sum_weight += inter.weight()
        return sum_weight

    # Эквивалентность
    def is_equal(self, other):
        # Проверка на подходящий тип интервала
        if not isinstance(other, (Interval, Intervals)):
            raise TypeError('Не возможно проверить на эквивалентность интервал ' + str(type(other)))
        if isinstance(other, Interval):
            other = Intervals('[' + other.__str__() + ']')
        result = False
        self.union()
        other = other.union()
        if (len(self.list_intervals) == len(other.list_intervals)) and (self.weight() == other.weight()):
            for i in range(len(self.list_intervals)):
                if self.list_intervals[i] != other.list_intervals[i]:
                    return False
                else:
                    result = True
        return result

    # Проверка на вхождение в интервалс
    def __contains__(self, item):
        # Проверка на подходящий тип интервала
        if not isinstance(item, (Interval, Intervals, int, float)):
            raise TypeError('Сравнение интервала не с интервалом не возможно')
        # Проверка интервалса в интервалсе
        if isinstance(item, Intervals):
            for j in item.list_intervals:
                for i in self.list_intervals:
                    if not i.__contains__(j):
                        return False
            return True
        # Проверка интервала и числа в интервалсе
        for i in self.list_intervals:
            if not i.__contains__(item):
                return False
        return True
