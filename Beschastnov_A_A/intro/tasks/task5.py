# Задача 5
# Вводится два целых числа a и b (a ≤ b). Найдите самое большее число на отрезке от a до b,
# кратное 7. Если такого числа нет выведите -1.
def find_nearest_divisible_in_interval_by_seven(a: int, b: int) -> int:
    if a > b:
        return -1

    result = 7 * int( b / 7 )

    if result < a or result > b:
        return -1

    return result

# Задача 5.1
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и «G».
# Нужно написать программу, которая получате на вход последовательность ДНК и на выходе
# отображает комлементарную ей
def gen_sequence_converter(gen_sequence: str) -> str:
    def get_mirror_gen(gen: str):
        GEN_MIRAGE_DICTIONARY = {
            "G": "C",
            "C": "G",
            "A": "T",
            "T": "A"
        }

        return GEN_MIRAGE_DICTIONARY.get(gen, "")

    converted_gen_sequence = ""

    for gen in gen_sequence:
        converted_gen_sequence += get_mirror_gen(gen)

    return converted_gen_sequence

# Задача 5*
# По данному числу N распечатайте все целые значения степени двойки, не превосходящие N,
# в порядке возрастания.
def power_of_two_generator(value_limit: int) -> int:
        pow = 0
        current_value = 2

        while current_value <= value_limit:
            yield current_value
            current_value = 2 ** pow
            pow += 1