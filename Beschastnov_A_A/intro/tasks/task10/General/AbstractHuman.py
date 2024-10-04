import abc

class AbstractHuman(metaclass=abc.ABCMeta):
    __first_name: str
    __second_name: str

    def __init__(self, first_name: str, second_name: str) -> None:
        self.__first_name = first_name
        self.__second_name = second_name

    def get_full_name(self) -> str:
        return self.__first_name + self.__second_name
