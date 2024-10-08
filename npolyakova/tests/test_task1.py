import unittest

from sample.task_1 import Task1


class TestTask1(unittest.TestCase):

    # positive
    def test_sum_digits_of_number_positive(self):
        res = Task1.multiply_digits_of_number("14962")
        assert res == 432

    def test_sum_digits_of_number_if_zero(self):
        res = Task1.multiply_digits_of_number("0")
        assert res == 0

    # negative
    def test_sum_digits_of_number_if_null(self):
        res = Task1.multiply_digits_of_number("")
        assert res.__eq__(None)

    def test_sum_digits_of_number_if_text(self):
        res = Task1.multiply_digits_of_number("text")
        assert res.__eq__(None)

    def test_sum_digits_of_number_if_no_number(self):
        res = Task1.multiply_digits_of_number("01")
        assert res.__eq__(None)


if __name__ == '__main__':
    unittest.main()
