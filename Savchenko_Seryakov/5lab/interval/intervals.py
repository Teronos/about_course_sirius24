"""
class for intervals
"""
from .interval import Interval


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
        new_intervals_srt = intervals_srt[1:-1]
        # parts = new_intervals_srt.split(', ')
        # for i in range(len(new_intervals_srt)):
        while len(new_intervals_srt) > 1:
            i = 0
            while new_intervals_srt[i] != ']' and new_intervals_srt[i] != ')' and new_intervals_srt[i] != '}':
                i += 1
            part = new_intervals_srt[:i + 1]
            inter = Interval.parser(part)
            intervals.list_intervals.append(inter)
            if len(new_intervals_srt[i + 1:]) > 3:
                new_intervals_srt = new_intervals_srt[i + 3:]
            else:
                new_intervals_srt = new_intervals_srt[i + 1:]

        return intervals

    # TODO - подумать как оно должно работать (это довавление а не сумма)
    def __add__(self, interval):
        self.list_intervals.append(interval)

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
