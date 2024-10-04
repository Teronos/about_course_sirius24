# Задача 4
# Вводится натуральное число N, а затем N целых чисел последовательности.
# Найдите количество минимальных элементов в последовательности

def count_minimal_elements_in_sequence() -> int:
    items = int(input())

    items_list = dict()

    for _ in range(items):
        target_item = int(input())

        items_list[target_item] = items_list.get(target_item, 0) + 1

    return min(items_list.values())

# Задача 4*
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что  φn=A . Если А не является числом Фибоначчи, выведите число -1.
def febonachi_position_finder(num: int) -> int:
    position = 0

    for febonachi_num in febonachi_generator(num):
        position += 1

    if febonachi_num != num:
        position = -1

    return position


def febonachi_generator(limit_num: int) -> int:
    target_num = 1
    before_num = 0

    while target_num <= limit_num:
        yield target_num
        tmp = target_num
        target_num += before_num
        before_num = tmp