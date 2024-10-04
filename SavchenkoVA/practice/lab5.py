from interval import Interval
import re

"""
Лабораторная 5:
Мини-библиотека реализующая интервалы, с функционалом их объединения, вычисления ширины,
проверки на эквивалентность. В состав библиотеке должен также входить парсер,
который считывает строковое представление интервалов и по нему создает нужные объекты.
Примеры работы с библиотекой:
* [ (0, 1), (1, 7), (7, 10] ] + {0, 1, 7} = [0, 10] (добавление точек)
* [5, 6] + (-2, 4) = [(-2, 4), [5, 6]] (объединение интервалов)
* (0, 12) + [ (-2, 1), (7, 10] ] = (-2, 12) (объединение интервалов в один)
"""


def parse_intervals(interval_str: str) -> list[Interval]:
    pattern = r'[\[\(](-?\d+),\s*(-?\d+)[\]\)]'
    matches = re.findall(pattern, interval_str)
    return [Interval(int(start), int(end)) for start, end in matches]


def lab5():
    interval1 = Interval(0, 1)
    interval2 = Interval(1, 7)
    interval3 = Interval(7, 10)

    # Добавление точек
    result1 = interval1 + {0, 1, 7}
    print(result1)  # (0, 10)

    # Объединение интервалов
    result2 = Interval(5, 6) + Interval(-2, 4)
    print(result2)  # (-2, 6)

    # Объединение интервалов в один
    result3 = Interval(0, 12) + [Interval(-2, 1), Interval(7, 10)]
    print(result3)  # (-2, 12)

    # Парсинг интервалов
    parsed_intervals = parse_intervals("[(0, 1), (1, 7), (7, 10)]")
    print(parsed_intervals)  # [(0, 1), (1, 7), (7, 10)]


if __name__ == "__main__":
    lab5()
