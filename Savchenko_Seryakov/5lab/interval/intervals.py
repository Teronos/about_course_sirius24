"""
class for intervals
"""
from .interval import Interval


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
