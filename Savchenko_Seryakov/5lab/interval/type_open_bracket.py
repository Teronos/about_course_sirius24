"""
class - enum for open bracket
"""
from enum import Enum


class TypeOpenBracket(Enum):
    ROUND = '('
    SQUARE = '['
    CURLY = '{'

    def __str__(self):
        return f'{self.value}'

    # def __eq__(self, other):
    #     if type(other) == str:
    #         return other == self.value
    #     return False
