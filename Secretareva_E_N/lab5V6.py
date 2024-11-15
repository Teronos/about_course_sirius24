import re

class Interval:
    Starting_point: float
    Ending_point: float
    Bracket_the_beginning: str
    Bracket_the_end: str
    def __init__(self, Starting_point: float, Ending_point: float, Bracket_the_beginning: str, Bracket_the_end: str):
            self.Starting_point = Starting_point
            self.Ending_point = Ending_point
            self.Bracket_the_beginning = Bracket_the_beginning
            self.Bracket_the_end = Bracket_the_end
            # self.uncrossed_intervals = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        start_str = f"{int(self.Starting_point) if self.Starting_point.is_integer() else self.Starting_point}"
        end_str = f"{int(self.Ending_point) if self.Ending_point.is_integer() else self.Ending_point}"
        return f"{self.Bracket_the_beginning}{start_str}, {end_str}{self.Bracket_the_end}"

    def intersects_with(self, other):

        if (self.Ending_point < other.Starting_point or other.Ending_point < self.Starting_point):
            return False
        if self.Ending_point == other.Starting_point:
            return self.Bracket_the_end == ']' or other.Bracket_the_beginning == '['
        if self.Starting_point == other.Ending_point:
            return self.Bracket_the_beginning == '[' or other.Bracket_the_end == ']'
        return True

    def intersection(self, other):

        if not self.intersects_with(other):
            return None

        if (self.Bracket_the_beginning == '[' or other.Bracket_the_beginning == '[') and self.Starting_point == other.Starting_point:
            new_start_bracket = '['
        else:
            new_start_bracket = self.Bracket_the_beginning if self.Starting_point <= other.Starting_point else other.Bracket_the_beginning
        if (self.Bracket_the_end == ']' or other.Bracket_the_end == ']') and self.Ending_point == other.Ending_point:
            new_end_bracket = ']'
        else:
            new_end_bracket = self.Bracket_the_end if self.Ending_point >= other.Ending_point else other.Bracket_the_end

        new_start = min(self.Starting_point, other.Starting_point)
        new_end = max(self.Ending_point, other.Ending_point)

        return Interval(new_start, new_end, new_start_bracket, new_end_bracket)

class Section:
    intervals: list[Interval]
    def __init__(self):
        self.intervals = []

    def __repr__(self):

        return self.__str__()

    def __str__(self):

        intervals_str = ", ".join(str(interval) for interval in self.intervals)
        return f"[{intervals_str}]"

    def add_interval(self, new_interval):
        if not self.intervals:
            self.intervals.append(new_interval)
            return

        last_interval = self.intervals[-1]
        intersection = last_interval.intersection(new_interval)
        if intersection:
            self.intervals[-1] = intersection
        else:
            self.intervals.append(new_interval)

    def add_interval_qe(self, new_interval):
            self.intervals.append(new_interval)

def Interval_processing(interval_str):

    intervals = []
    intervals_eq = []

    intervals_matches = parse_intervals(interval_str)
    for match in intervals_matches:
        left_bracket, start, end, right_bracket = match
        intervals.append(Interval(float(start), float(end), str(left_bracket), str(right_bracket)))

    points_matches = parse_point(interval_str)

    for point in points_matches:
        point_value = float(point)
        intervals.append(Interval(point_value, point_value, '[', ']'))

    intervals.sort(
        key=lambda interval: (
            interval.Starting_point,
            interval.Ending_point,
            interval.Bracket_the_beginning == '(',
            interval.Bracket_the_end == ')'
        )
    )
    section = Section()
    for interval in range(len(intervals)):
        section.add_interval(intervals[interval])

    str_eq = get_eq(interval_str)
    points_matches_eq = parse_intervals(str_eq)

    for match in points_matches_eq:
        left_bracket, start, end, right_bracket = match
        intervals_eq.append(Interval(float(start), float(end), str(left_bracket), str(right_bracket)))

    if len(intervals_eq) == 0:
        return section

    section_eq = Section()
    for interval in range(len(intervals_eq)):
        section_eq.add_interval_qe(intervals_eq[interval])

    return str(section_eq) == str(section)

def parse_intervals(interval_str):

    intervals_matches = re.findall(r'([\[\(])\s*(-?\d+)\s*,\s*(-?\d+)\s*([\]\)])', interval_str)

    return intervals_matches

def parse_point(interval_str):

    points_pattern = re.findall(r'(?<=\{|\s|,)-?\d+(?:\.\d+)?(?=\s*[,}])', interval_str)

    return points_pattern

def get_eq(interval_str):
    result_str = ''

    parts = interval_str.split('=')

    if len(parts) > 1:
        result_str += parts[-1]

    return result_str


# interval_str = "(0, 12) + [ (-2, 1), (7, 10] ]"
# parsed_intervals = parse(interval_str)
interval_str = "[ (0, 1), (1, 7), (7, 10] ] + {0, 1, 7}"
parsed_intervals2 = Interval_processing(interval_str)
interval_str = "[5, 6] + (-2, 4)"
parsed_intervals3 = Interval_processing(interval_str)
interval_str = "[ (0, 1), (1, 7), (7, 10] ] + {0, 1, 7} = [0, 10]"
# test = parse_eq(interval_str)

# print(test)
# ll = parse_intervals(test)
# print(ll)


parsed_intervals4 = Interval_processing(interval_str)
# # print(parsed_intervals)
print(parsed_intervals2)
print(parsed_intervals3)
print(parsed_intervals4)