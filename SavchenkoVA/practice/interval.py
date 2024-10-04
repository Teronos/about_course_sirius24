class Interval:
    start: int
    end: int

    def __init__(self, start: int, end: int) -> None:
        if start > end:
            raise ValueError("Начало интервала не может быть больше конца.")
        self.start = start
        self.end = end

    def width(self) -> int:
        return self.end - self.start

    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(min(self.start, other.start), max(self.end, other.end))
        elif isinstance(other, set):
            points = sorted(other)
            new_start = min(points + [self.start])
            new_end = max(points + [self.end])
            return Interval(new_start, new_end)
        elif isinstance(other, list):
            new_start = min(self.start, *[i.start for i in other])
            new_end = max(self.end, *[i.end for i in other])
            return Interval(new_start, new_end)
        else:
            raise TypeError("Неподдерживаемый тип для сложения.")

    def __eq__(self, other) -> bool:
        return self.start == other.start and self.end == other.end

    def __repr__(self) -> str:
        return f"({self.start}, {self.end})"
