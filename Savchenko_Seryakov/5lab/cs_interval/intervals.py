
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
