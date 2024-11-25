"""
class - enum for close bracket
"""
from enum import Enum


class TypeClosedBracket(Enum):
    ROUND = ')'
    SQUARE = ']'
    CURLY = '}'

    def __str__(self):
        return f'{self.value}'
