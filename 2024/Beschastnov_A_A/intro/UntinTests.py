import io
import sys
import unittest

import tasks.task1
import tasks.task2
import tasks.task3
import tasks.task4
import tasks.task5
import tasks.task6
import tasks.task7
import tasks.task8
import tasks.task9
from tasks.task10.Company.Company import Company

class TestTasks(unittest.TestCase):
  def test_task1(self):
    # Задача 1
    sys.stdin = io.StringIO("745")
    result_sum = tasks.task1.sum_nubmer_sequences()
    self.assertEqual(result_sum, 16)

    # Задача 1*
    sys.stdin = io.StringIO("14962")
    result_mul = tasks.task1.mul_nubmer_sequences()
    sys.stdin = sys.__stdin__

    self.assertEqual(result_mul, 432)
  def test_task2(self):
    # Задача 2
    sys.stdin = io.StringIO("843")
    result_reverse = tasks.task2.my_reverse()
    self.assertEqual(result_reverse, 348)

    # Задача 2*
    sys.stdin = io.StringIO("531893")
    result_sum_even_and_odd = tasks.task2.sum_even_and_odd_nubmer()
    sys.stdin = sys.__stdin__

    self.assertEqual(result_sum_even_and_odd, (15, 29))
  def test_task3(self):
    # Задача 3
    sys.stdin = io.StringIO("5\n1\n8\n100\n0\n12")
    result_count_numbers_equel_zero = tasks.task3.count_numbers_equel_zero()
    self.assertEqual(result_count_numbers_equel_zero, 1)

    # Задача 3*
    sys.stdin = io.StringIO("6\n6\n3\n2\n42\n5\n12")
    result_average_number_multiple_three = tasks.task3.average_number_multiple_three()
    sys.stdin = sys.__stdin__

    self.assertEqual(result_average_number_multiple_three, 15.75)
  def test_task4(self):
    # Задача 4
    sys.stdin = io.StringIO("3\n21\n11\n4")
    result_count_minimal_elements_in_sequence = tasks.task4.count_minimal_elements_in_sequence()
    sys.stdin = sys.__stdin__

    self.assertEqual(result_count_minimal_elements_in_sequence, 1)

    # Задача 4*
    self.assertEqual(tasks.task4.febonachi_position_finder(8), 6)
  def test_task5(self):
    # Задача 5
    self.assertEqual((tasks.task5.find_nearest_divisible_in_interval_by_seven(100, 500)), 497)
    # Задача 5.1
    self.assertEqual(tasks.task5.gen_sequence_converter("GTAT"), "CATA")

    # Задача 5*
    for value in tasks.task5.power_of_two_generator(50):
      result_power_of_two_generator_last_value = value

    self.assertEqual(result_power_of_two_generator_last_value, 32)
  def test_task6(self):
    # Задача 6
    sys.stdin = io.StringIO("5\n2\n3\n56\n45\n21")
    self.assertEqual(tasks.task6.print_max_elem_from_list(), 56)

    # Задача 6*
    sys.stdin = io.StringIO("5\n1\n2\n3\n-1\n-4")
    self.assertEqual(tasks.task6.count_of_positive_numbers_from_sequence(), 3)
    sys.stdin = sys.__stdin__
  def test_task7(self):
    # Задача 7
    sys.stdin = io.StringIO("5\n38 24 800 8 16")
    self.assertEqual(tasks.task7.print_sum_of_two_digit_numbers_from_sequence(), 40)

    # Задача 7*
    sys.stdin = io.StringIO("1\n3\n3\n1\n0")
    self.assertEqual(tasks.task7.get_count_biggest_num_in_sequences(), 2)
    sys.stdin = sys.__stdin__
  def test_task8(self):
    # Задача 8
    self.assertEqual(tasks.task8.get_common_digits(564, 8954), "5 4")
    # Задача 8*
    self.assertEqual(tasks.task8.my_sort([ [1,2,3], [4,5,6], [7,8,9] ]), [1,2,3,6,9,8,7,4,5])
  def test_task9(self):
    # Задача 9
    p1 = tasks.task9.Point()
    p2 = tasks.task9.Point()
    p1.set_coordinates(1, 2)
    p2.set_coordinates(4, 6)

    original_stdout = sys.stdout

    captured_output = io.StringIO()
    sys.stdout = captured_output

    p1.get_distance(10)

    sys.stdout = original_stdout

    self.assertEqual(p1.get_distance(p2), 5.0)
    self.assertEqual(captured_output.getvalue().strip(), "Передана не точка")

    # Задача 9.1
    person = tasks.task9.Person("Anton", "Beschastnov", 21)

    self.assertEqual(person.full_name(), "Beschastnov Anton")
    self.assertEqual(person.is_adult(), True)

    hp = tasks.task9.Laptop('hp', '15-bw0xx', 57000)

    # Задача 9*
    self.assertEqual(hp.price, 57000)
    self.assertEqual(hp.laptop_name(), "hp 15-bw0xx")

  def test_task10(self):
    # Задача 10*
    vk = Company("vk", 200)

    director = vk.create_director("Vova", "Novaselchev", 20)

    empl1 = vk.create_employee("Petya1", "Novaselchev", 10)

    empl2 = vk.create_employee("Petya2", "Novaselchev", 30)

    self.assertEqual(vk.get_balance(), 200)

    vk.fulfill_promise()

    self.assertEqual(director.check_promises(), True)

    self.assertEqual(vk.get_balance(), 140)

    vk.set_profit(-10000)

    self.assertEqual(vk.get_balance(), -9860)

    vk.fulfill_promise()

    self.assertEqual(director.check_promises(), False)
    self.assertEqual(director.get_promise().get_company_debt(), 20)

if __name__ == "__main__":
  unittest.main()

