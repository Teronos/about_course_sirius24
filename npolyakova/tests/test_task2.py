import unittest

from sample.task_2 import Task2


class TestTask1(unittest.TestCase):

    # positive
    def test_sum_digits_of_number_positive(self):
        res = Task2.sum_digits_of_number("531893")
        assert res == "1514"

    def test_sum_digits_of_number_if_zero(self):
        res = Task2.sum_digits_of_number("0")
        assert res == "0"

    def test_sum_digits_of_number_if_one_digit(self):
        res = Task2.sum_digits_of_number("1")
        assert res == "10"

    # negative
    def test_sum_digits_of_number_if_null(self):
        res = Task2.sum_digits_of_number("")
        assert res.__eq__(None)

    def test_sum_digits_of_number_if_text(self):
        res = Task2.sum_digits_of_number("text")
        assert res.__eq__(None)

    def test_sum_digits_of_number_if_no_number(self):
        res = Task2.sum_digits_of_number("01")
        assert res.__eq__(None)


if __name__ == '__main__':
    unittest.main()
