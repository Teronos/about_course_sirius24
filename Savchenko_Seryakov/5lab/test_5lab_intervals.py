import unittest
import interval

class TestIntervals(unittest.TestCase):


    # Test on create and parser
    # True
    def test_create_intervals_1(self):
        try:
            inter = interval.Intervals('[[0, 10]]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_1_forgot_bracket(self):
        try:
            inter = interval.Intervals('[0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_2(self):
        try:
            inter = interval.Intervals('[[0, 10], (12, 20)]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_much(self):
        try:
            inter = interval.Intervals('[[0, 10], (12, 20), [22, 27), (30, 32]]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_simple(self):
        try:
            inter = interval.Intervals('[0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_multiple(self):
        try:
            inter = interval.Intervals('[0, 5], (5, 10], [15, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_single_point(self):
        try:
            inter = interval.Intervals('{5}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_combined(self):
        try:
            inter = interval.Intervals('[0, 5], {10}, [15, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_floats(self):
        try:
            inter = interval.Intervals('[0.0, 5.5], {3.3}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_intervals_nested(self):
        try:
            inter = interval.Intervals('[0, 10], [10, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_point(self):
        try:
            inter = interval.Intervals('[{10}]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    # False
    def test_false_create_empty(self):
        try:
            inter = interval.Intervals('')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))
        except:
            self.assertTrue(False)

    def test_false_create_empty_list(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))
        except:
            self.assertTrue(False)

    def test_false_create_a(self):
        try:
            inter = interval.Intervals('[[0, a], (12, 20)]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали число для интервала',))
        except:
            self.assertTrue(False)

    # def test_false_create_forgot_bracket(self):
    #     try:
    #         inter = interval.Intervals('[[0, 10, (12, 20)]')
    #         self.assertTrue(False)
    #     except ValueError as e:
    #         self.assertEqual(e.args, ('Вы забыли закрывающую скобку ), ] или }',))
    #     except:
    #         self.assertTrue(False)

    # Test intervals to str
    # True
    def test_interval_to_str(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.__str__(), '[0, 11]')

    def test_intervals_to_str_single_interval(self):
        inter = interval.Intervals('[0, 11]')
        self.assertEqual(inter.__str__(), '[0, 11]')

    def test_intervals_to_str_multiple_intervals(self):
        inter = interval.Intervals('[[0, 5], (5, 10], {15}]')
        self.assertEqual(inter.__str__(), '[[0, 5], (5, 10], {15}]')

    def test_intervals_to_str_single_point(self):
        inter = interval.Intervals('{5}')
        self.assertEqual(inter.__str__(), '{5}')

    def test_intervals_to_str_combined(self):
        inter = interval.Intervals('[[0, 3], {5}, (6, 8]]')
        self.assertEqual(inter.__str__(), '[[0, 3], {5}, (6, 8]]')

    def test_intervals_to_str_disjoint_intervals(self):
        inter = interval.Intervals('[[0, 5], [10, 15], [20, 25]]')
        self.assertEqual(inter.__str__(), '[[0, 5], [10, 15], [20, 25]]')

    def test_intervals_to_str_empty_interval_list(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)  # Если пустой интервал создается без ошибки, тест провален
        except ValueError:
            self.assertTrue(True)  # Ожидаем исключение ValueError

    # __repr__

    # Test weight
    # True
    def test_weight_interval(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_single_interval(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_multiple_intervals(self):
        inter = interval.Intervals('[0, 5], [10, 15], [20, 25]')
        self.assertEqual(inter.weight(), 15)

    def test_weight_overlapping_intervals(self):
        inter = interval.Intervals('[0, 10], [5, 15]')
        self.assertEqual(inter.weight(), 15)

    def test_weight_overlapping_intervals_2(self):
        inter = interval.Intervals('[0, 20], [5, 15]')
        self.assertEqual(inter.weight(), 20)

    def test_weight_single_point(self):
        inter = interval.Intervals('{5}')
        self.assertEqual(inter.weight(), 0)

    def test_weight_disjoint_intervals_with_points(self):
        inter = interval.Intervals('[0, 5], {6}, [7, 10]')
        self.assertEqual(inter.weight(), 8)

    def test_weight_complex_intervals(self):
        inter = interval.Intervals('[0, 5], [6, 10), {12}, (15, 20]')
        self.assertEqual(inter.weight(), 14)

    # Test union
    # True
    def test_1_otrezok(self):
        inter = interval.Intervals('[[0, 5]]')
        self.assertEqual(str(inter.union()), '[0, 5]')

    def test_1_interval(self):
        inter = interval.Intervals('[(0, 5)]')
        self.assertEqual(str(inter.union()), '(0, 5)')

    def test_3_pol_interval(self):
        inter = interval.Intervals('[(0, 1], (1, 3], (3, 10]]')
        self.assertEqual(str(inter.union()), '(0, 10]')

    def test_2_pol_interval(self):
        inter = interval.Intervals('[(0, 5], [5, 10]]')
        self.assertEqual(str(inter.union()), '(0, 10]')

    def test_2_otrezka_union(self):
        inter = interval.Intervals('[[0, 5], [6, 10]]')
        self.assertEqual(str(inter.union()), '[[0, 5], [6, 10]]')

    def test_big_last(self):
        inter = interval.Intervals('[[0, 5], [6, 10], [0, 15]]')
        self.assertEqual(str(inter.union()), '[0, 15]')

    def test_big_first(self):
        inter = interval.Intervals('[[0, 15], (0, 7], [6, 10], (12, 15)]')
        self.assertEqual(str(inter.union()), '[0, 15]')

    def test_add_point(self):
        inter = interval.Intervals('[[0, 5), (5, 10], {10}]')
        self.assertEqual(str(inter.union()), '[[0, 5), (5, 10]]')

    def test_add_points(self):
        inter = interval.Intervals('[(0, 1), (1, 7), (7, 10], {0, 1, 7}]')
        self.assertEqual(str(inter.union()), '[0, 10]')

    def test_no_sort(self):
        inter = interval.Intervals('[(0, 1), [5, 10], [0, 20), (1, 7), {1}')
        self.assertEqual(str(inter.union()), '[0, 20)')



    # Test +
    # True
    def test_add_1_1_interseс(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_otrezok_add_otrezok_1(self):
        try:
            inter1 = interval.Intervals('[0, 5]')
            inter2 = interval.Intervals('[5, 10]')
            self.assertEqual(str(inter1 + inter2), '[0, 10]')
        except:
            self.assertFalse(True)

    def test_add_1_1_union(self):
        inter1 = interval.Intervals('[0, 5)')
        inter2 = interval.Intervals('(5, 10]')
        self.assertEqual(str(inter1.__add__(inter2)), '[[0, 5), (5, 10]]')

    def test_add_2_2(self):
        inter1 = interval.Intervals('[0, 5], (15, 20]')
        inter2 = interval.Intervals('[5, 15], (18, 22]')
        self.assertEqual(str(inter1 + inter2), '[0, 22]')

    def test_add_1_2(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10], (10, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_add_simple_union(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10], (10, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_add_no_overlap(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[10, 15]')
        self.assertEqual(str(inter1 + inter2), '[[0, 5], [10, 15]]')

    def test_add_partial_overlap(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[5, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 15]')

    def test_add_point_to_interval(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Interval('{5}')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_add_point_outside(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Interval('{15}')
        self.assertEqual(str(inter1 + inter2), '[[0, 10], {15}]')

    # TODO посмотреть точки вместе
    def test_add_single_point_intervals(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{10}')
        self.assertEqual(str(inter1 + inter2), '[{5}, {10}]')

    def test_add_single_point_merge(self):
        inter1 = interval.Intervals('[0, 5)')
        inter2 = interval.Interval('{5}')
        self.assertEqual(str(inter1 + inter2), '[0, 5]')

    def test_add_nested_intervals(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_add_disjoint_intervals(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[10, 15]')
        self.assertEqual(str(inter1 + inter2), '[[0, 5], [10, 15]]')

    def test_add_multiple_overlaps(self):
        inter1 = interval.Intervals('[0, 5], [10, 15]')
        inter2 = interval.Intervals('[5, 10], [12, 20]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_add_different_brackets(self):
        inter1 = interval.Intervals('(0, 5)')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '(0, 10]')
    # TODO Ошибка, если вводятся пустые
    # def test_add_empty_intervals(self):
    #     inter1 = interval.Intervals('[0, 10]')
    #     inter2 = interval.Intervals('[]')
    #     self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_add_float_intervals(self):
        inter1 = interval.Intervals('[0.0, 5.5]')
        inter2 = interval.Intervals('[5.5, 10.0]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    # TODO Ошибка, если вводятся пустые
    # def test_add_point_to_empty(self):
    #     inter1 = interval.Intervals('[]')
    #     inter2 = interval.Interval('{5}')
    #     self.assertEqual(str(inter1 + inter2), '{5}')

    def test_add_large_overlaps(self):
        inter1 = interval.Intervals('[0, 100]')
        inter2 = interval.Intervals('[50, 150]')
        self.assertEqual(str(inter1 + inter2), '[0, 150]')

    def test_add_identical_intervals(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_add_adjacent_intervals(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    # False

    # TODO is_equal
    # True
    def test_equal_simple(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 10]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_different_order(self):
        inter1 = interval.Intervals('[0, 5], [10, 15]')
        inter2 = interval.Intervals('[10, 15], [0, 5]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_nested(self):
        inter1 = interval.Intervals('[0, 15]')
        inter2 = interval.Intervals('[0, 10], [10, 15]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_single_point(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{5}')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_mixed_types(self):
        inter1 = interval.Intervals('[0, 5], {10}')
        inter2 = interval.Intervals('{10}, [0, 5]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_disjoint_union(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 5], [5, 10]')
        self.assertTrue(inter1.is_equal(inter2))

    # TODO Ошибка, если вводятся пустые
    # def test_equal_identical_empty(self):
    #     inter1 = interval.Intervals('[]')
    #     inter2 = interval.Intervals('[]')
    #     self.assertTrue(inter1.is_equal(inter2))

    def test_equal_floats(self):
        inter1 = interval.Intervals('[0.0, 5.5]')
        inter2 = interval.Intervals('[0.0, 5.5]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_equal_with_union(self):
        inter1 = interval.Intervals('[0, 5], [5, 10]')
        inter2 = interval.Intervals('[0, 10]')
        self.assertTrue(inter1.is_equal(inter2))


    # False
    def test_not_equal_simple(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[5, 15]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_different_weights(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[0, 5], [10, 15]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_different_brackets(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('(0, 10]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_single_point(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{10}')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_mixed_types(self):
        inter1 = interval.Intervals('[0, 5], {10}')
        inter2 = interval.Intervals('[0, 5], [10, 15]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_partial_overlap(self):
        inter1 = interval.Intervals('[0, 5), (5, 15]')
        inter2 = interval.Intervals('[0, 15]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_floats(self):
        inter1 = interval.Intervals('[0.0, 5.5]')
        inter2 = interval.Intervals('[0.0, 5.4]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_not_equal_different_length(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 5], [10, 15]')
        self.assertFalse(inter1.is_equal(inter2))

    # TODO Test contains (in)
    # True
    def test_intervals_contains_point(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertTrue(5 in inter)

    def test_intervals_contains_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        sub_inter = interval.Interval('[2, 8]')
        self.assertTrue(sub_inter in inter)

    #
    def test_intervals_contains_single_point(self):
        inter = interval.Intervals('[[0, 10]], {15}')
        self.assertTrue(15 in inter)

    #
    def test_intervals_contains_intervals(self):
        inter = interval.Intervals('[[0, 10]], [[15, 20]]')
        sub_inter = interval.Intervals('[[3, 7]], [[16, 18]]')
        self.assertTrue(sub_inter in inter)

    def test_intervals_contains_point_at_bounds(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertTrue(0 in inter)
        self.assertTrue(10 in inter)

    #TODO Ошибка, если вводятся пустые
    def test_intervals_contains_empty(self):
        inter = interval.Intervals('[[0, 10]]')
        empty_inter = interval.Intervals('[]')
        self.assertTrue(empty_inter in inter)

    # False
    def test_intervals_not_contains_point(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertFalse(15 in inter)

    def test_intervals_not_contains_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        sub_inter = interval.Interval('[11, 20]')
        self.assertFalse(sub_inter in inter)

    def test_intervals_not_contains_point_out_of_bounds(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertFalse(-1 in inter)
        self.assertFalse(11 in inter)
    #
    def test_intervals_not_contains_intervals(self):
        inter = interval.Intervals('[[0, 10]], [[15, 20]]')
        sub_inter = interval.Intervals('[[12, 14]]')
        self.assertFalse(sub_inter in inter)
    #
    def test_intervals_not_contains_point_in_gap(self):
        inter = interval.Intervals('[[0, 10]], [[15, 20]]')
        self.assertFalse(12 in inter)

    # TODO Ошибка, если вводятся пустые
    def test_intervals_not_contains_empty(self):
        inter = interval.Intervals('[[0, 10]]')
        empty_inter = interval.Intervals('[]')
        self.assertFalse(empty_inter in inter)  # если интервал не допускает пустых значений


if __name__ == '__main__':
    unittest.main()