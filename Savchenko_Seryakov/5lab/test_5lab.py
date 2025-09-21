import unittest
import interval


class TestIntervalIntervals(unittest.TestCase):

    # Test on create and parser
    # Interval
    # True
    def test_create_interval(self):
        try:
            inter = interval.Interval('[0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_otrezok(self):
        try:
            inter = interval.Interval('(0, 10)')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_int_ot(self):
        try:
            inter = interval.Interval('[0, 10)')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_ot_int(self):
        try:
            inter = interval.Interval('(0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_point(self):
        try:
            inter = interval.Interval('{10}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    # Intervals
    # True
    def test_create_list_interval(self):
        try:
            inter = interval.Intervals('[[0, 10]]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_forgot_bracket(self):
        try:
            inter = interval.Intervals('[0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_two(self):
        try:
            inter = interval.Intervals('[[0, 10], (12, 20)]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_much(self):
        try:
            inter = interval.Intervals('[[0, 10], (12, 20), [22, 27), (30, 32]]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_simple(self):
        try:
            inter = interval.Intervals('[0, 10]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_union(self):
        try:
            inter = interval.Intervals('[0, 5], (5, 10], [15, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_one_point(self):
        try:
            inter = interval.Intervals('{5}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_one_minus_point(self):
        try:
            inter = interval.Intervals('{-5}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_combination(self):
        try:
            inter = interval.Intervals('[0, 5], {10}, [15, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_float(self):
        try:
            inter = interval.Intervals('[0.0, 5.5], {3.3}')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_adds(self):
        try:
            inter = interval.Intervals('[0, 10], [10, 20]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_create_list_interval_with_point(self):
        try:
            inter = interval.Intervals('[{10}]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    # Interval
    # False
    def test_false_create_point(self):
        try:
            inter = interval.Interval('10}')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('В вашем интервале не хватает открывающей скобки [, ( или {',))
        except:
            self.assertTrue(False)

    def test_false_create(self):
        try:
            inter = interval.Interval('')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой интервал',))
        except:
            self.assertTrue(False)

    def test_false_create_a(self):
        try:
            inter = interval.Interval('(a')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали число для интервала',))
        except:
            self.assertTrue(False)

    def test_false_create_pol_interval(self):
        try:
            inter = interval.Interval('(10, ')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали второе число для интервала',))
        except:
            self.assertTrue(False)

    def test_false_create_interval_a(self):
        try:
            inter = interval.Interval('(10, a')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали второе число для интервала',))
        except:
            self.assertTrue(False)

    def test_false_create_interval(self):
        try:
            inter = interval.Interval('(10, 11')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('В вашем интервале не хватает закрывающей скобки ], ) или }',))
        except:
            self.assertTrue(False)

    def test_false_create_invert_interval(self):
        try:
            inter = interval.Interval('[100, 11]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    # Intervals
    # False
    def test_false_create_empty_list(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))
        except:
            self.assertTrue(False)

    def test_false_create_empty(self):
        try:
            inter = interval.Intervals('')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))
        except:
            self.assertTrue(False)

    def test_false_create_list_a(self):
        try:
            inter = interval.Intervals('[[0, a], (12, 20)]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали второе число для интервала',))
        except:
            self.assertTrue(False)

    def test_false_create_list_forgot_bracket(self):
        try:
            inter = interval.Intervals('[[0, 10, (12, 20)]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('В вашем интервале не хватает закрывающей скобки ], ) или }',))
        except:
            self.assertTrue(False)

    # Test interval to str
    # Interval
    # True
    def test_interval_to_str(self):
        inter = interval.Interval('[0, 11]')
        self.assertEqual(inter.__str__(), '[0, 11]')

    def test_otrezok_to_str(self):
        inter = interval.Interval('(0, 11)')
        self.assertEqual(inter.__str__(), '(0, 11)')

    def test_inter_otrez_to_str(self):
        inter = interval.Interval('[0, 11)')
        self.assertEqual(inter.__str__(), '[0, 11)')

    def test_otrez_inter_to_str(self):
        inter = interval.Interval('(0, 11]')
        self.assertEqual(inter.__str__(), '(0, 11]')

    def test_int_point_to_str(self):
        inter = interval.Interval('{11}')
        self.assertEqual(inter.__str__(), '{11}')

    # Intervals
    # True
    def test_list_interval_to_str(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.__str__(), '[0, 11]')

    def test_list_interval_to_str_interval(self):
        inter = interval.Intervals('[0, 11]')
        self.assertEqual(inter.__str__(), '[0, 11]')

    def test_list_interval_to_str_union(self):
        inter = interval.Intervals('[[0, 5], (5, 10], {15}]')
        self.assertEqual(inter.__str__(), '[[0, 5], (5, 10], {15}]')

    def test_list_interval_to_str_one_point(self):
        inter = interval.Intervals('{5}')
        self.assertEqual(inter.__str__(), '{5}')

    def test_list_interval_to_str_combination(self):
        inter = interval.Intervals('[[0, 3], {5}, (6, 8]]')
        self.assertEqual(inter.__str__(), '[[0, 3], {5}, (6, 8]]')

    def test_list_interval_to_str_mush(self):
        inter = interval.Intervals('[[0, 5], [10, 15], [20, 25]]')
        self.assertEqual(inter.__str__(), '[[0, 5], [10, 15], [20, 25]]')

    def test_list_interval_to_str_empty(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)  # Если пустой интервал создается без ошибки, тест провален
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))  # Ожидаем исключение ValueError
        except:
            self.assertTrue(False)

    # Test interval to repr
    # Interval
    # True
    def test_interval_to_repr(self):
        inter = interval.Interval('[0, 11]')
        self.assertEqual(inter.__repr__(), '[0, 11]')

    def test_otrezok_to_repr(self):
        inter = interval.Interval('(0, 11)')
        self.assertEqual(inter.__repr__(), '(0, 11)')

    def test_inter_otrez_to_repr(self):
        inter = interval.Interval('[0, 11)')
        self.assertEqual(inter.__repr__(), '[0, 11)')

    def test_otrez_inter_to_repr(self):
        inter = interval.Interval('(0, 11]')
        self.assertEqual(inter.__repr__(), '(0, 11]')

    def test_point_to_repr(self):
        inter = interval.Interval('{11}')
        self.assertEqual(inter.__repr__(), '{11}')

    # Intervals
    # True
    def test_list_interval_to_repr(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.__repr__(), '[0, 11]')

    def test_list_interval_to_repr_interval(self):
        inter = interval.Intervals('[0, 11]')
        self.assertEqual(inter.__repr__(), '[0, 11]')

    def test_list_interval_to_repr_union(self):
        inter = interval.Intervals('[[0, 5], (5, 10], {15}]')
        self.assertEqual(inter.__repr__(), '[[0, 5], (5, 10], {15}]')

    def test_list_interval_to_repr_one_point(self):
        inter = interval.Intervals('{5}')
        self.assertEqual(inter.__repr__(), '{5}')

    def test_list_interval_to_repr_combination(self):
        inter = interval.Intervals('[[0, 3], {5}, (6, 8]]')
        self.assertEqual(inter.__repr__(), '[[0, 3], {5}, (6, 8]]')

    def test_list_interval_to_repr_mush(self):
        inter = interval.Intervals('[[0, 5], [10, 15], [20, 25]]')
        self.assertEqual(inter.__repr__(), '[[0, 5], [10, 15], [20, 25]]')

    def test_list_interval_to_repr_empty(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)  # Если пустой интервал создается без ошибки, тест провален
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))  # Ожидаем исключение ValueError
        except:
            self.assertTrue(False)

    # Test weight
    # Interval
    # True
    def test_weight_interval(self):
        inter = interval.Interval('[0, 11]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_otrezok(self):
        inter = interval.Interval('(0, 11)')
        self.assertEqual(inter.weight(), 11)

    def test_weight_inter_otrez(self):
        inter = interval.Interval('[0, 11)')
        self.assertEqual(inter.weight(), 11)

    def test_weight_otrez_inter(self):
        inter = interval.Interval('(0, 11]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_point(self):
        inter = interval.Interval('{11}')
        self.assertEqual(inter.weight(), 0)

    # Intervals
    # True
    def test_weight_list_interval(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_single_list_interval(self):
        inter = interval.Intervals('[0, 11]')
        self.assertEqual(inter.weight(), 11)

    def test_weight_mush_list_interval(self):
        inter = interval.Intervals('[0, 5], [10, 15], [20, 25]')
        self.assertEqual(inter.weight(), 15)

    def test_weight_adds_list_interval(self):
        inter = interval.Intervals('[0, 10], [5, 15]')
        self.assertEqual(inter.weight(), 15)

    def test_weight_union_list_interval(self):
        inter = interval.Intervals('[0, 20], [5, 15]')
        self.assertEqual(inter.weight(), 20)

    def test_weight_single_point_list(self):
        inter = interval.Intervals('{5}')
        self.assertEqual(inter.weight(), 0)

    def test_weight_list_interval_with_points(self):
        inter = interval.Intervals('[0, 5], {6}, [7, 10]')
        self.assertEqual(inter.weight(), 8)

    def test_weight_list_interval_all(self):
        inter = interval.Intervals('[0, 5], [6, 10), {12}, (15, 20]')
        self.assertEqual(inter.weight(), 14)

    # Test ==
    # Interval
    # True
    def test_interval_eq_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('[0, 11]')
        self.assertTrue(inter1 == inter2)

    def test_otrezok_eq_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('(0, 11)')
        self.assertTrue(inter1 == inter2)

    def test_point_eq_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 == inter2)

    def test_pol_interval_eq_pol_interval(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Interval('[0, 11)')
        self.assertTrue(inter1 == inter2)

    def test_pol_otrezok_eq_pol_otrezok(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Interval('(0, 11]')
        self.assertTrue(inter1 == inter2)

    def test_interval_eq_point(self):
        inter1 = interval.Interval('[11, 11]')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 == inter2)

    # Interval == Intervals
    # True
    def test_interval_eq_list_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Intervals('[[0, 11]]')
        self.assertTrue(inter1 == inter2)

    def test_otrezok_eq_list_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Intervals('[(0, 11)]')
        self.assertTrue(inter1 == inter2)

    def test_point_eq_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 == inter2)

    def test_pol_interval_eq_list_pol_interval(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Intervals('[[0, 11)]')
        self.assertTrue(inter1 == inter2)

    def test_pol_otrezok_eq_list_pol_otrezok(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Intervals('[(0, 11]]')
        self.assertTrue(inter1 == inter2)

    def test_interval_eq_list_point(self):
        inter1 = interval.Interval('[11, 11]')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 == inter2)

    # Interval
    # False
    def test_false_interval_eq_otrezok(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('(0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_pol_otrezok(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_pol_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_point(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_interval(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('[0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_pol_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_pol_interval(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_point(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_interval(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Interval('[0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_otrezok(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Interval('(0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_pol_interval(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_point(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_interval(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Interval('[0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_pol_otrezok(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_otezok(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Interval('(0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_point(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_interval(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('[0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_pol_otrezok(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_pol_interval(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_otrezok(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('(0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_a(self):
        inter1 = interval.Interval('{11}')
        try:
            self.assertFalse(inter1 == 'a')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    def test_false_interval_eq_a(self):
        inter1 = interval.Interval('[0, 11]')
        try:
            self.assertFalse(inter1 == 'a')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    def test_false_pol_interval_eq_a(self):
        inter1 = interval.Interval('[0, 11)')
        try:
            self.assertFalse(inter1 == 'a')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    def test_false_otrezok_eq_a(self):
        inter1 = interval.Interval('(0, 11)')
        try:
            self.assertFalse(inter1 == 'a')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    def test_false_pol_otrezok_eq_a(self):
        inter1 = interval.Interval('(0, 11]')
        try:
            self.assertFalse(inter1 == 'a')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    # Interval == Intervals
    # False
    def test_false_interval_eq_list_otrezok(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Intervals('[(0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_list_pol_otrezok(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Intervals('[(0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_list_pol_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Intervals('[[0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_interval_eq_list_point(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Intervals('[{11}]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_list_interval(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Intervals('[[0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_list_pol_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Intervals('[(0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_list_pol_interval(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Intervals('[[0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_otrezok_eq_list_point(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Intervals('[{11}]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_list_interval(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Intervals('[[0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_list_otrezok(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Intervals('[(0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_list_pol_interval(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Intervals('[[0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_otrezok_eq_list_point(self):
        inter1 = interval.Interval('(0, 11]')
        inter2 = interval.Intervals('[{11}]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_list_interval(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Intervals('[[0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_list_pol_otrezok(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Intervals('[(0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_list_otezok(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Intervals('[(0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_pol_interval_eq_list_point(self):
        inter1 = interval.Interval('[0, 11)')
        inter2 = interval.Intervals('[{11}]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_list_interval(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[[0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_list_pol_otrezok(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[(0, 11]]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_list_pol_interval(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[[0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_list_otrezok(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[(0, 11)]')
        self.assertFalse(inter1 == inter2)

    def test_false_point_eq_big_list(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[(0, 11), {11}]')
        self.assertFalse(inter1 == inter2)

    # Test <
    # Interval
    # True
    def test_otrezok_lt_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_pol_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_point(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_otrezok(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_pol_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_pol_otrezok(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_point(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_otrezok(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_pol_otrezok(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_point(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_interval(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_pol_interval(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_point(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_interval(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_otrezok(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_pol_interval(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('[1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_pol_otrezok(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('(1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_point(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('{11}')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[0, 7]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(0, 7]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[0, 7]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(0, 7]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('(0, 7]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('[0, 7]')
        self.assertTrue(inter1 < inter2)

    # Interval < Intervals
    # True
    def test_otrezok_lt_list_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[(1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[(1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_list_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_list_pol_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[[1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_list_point(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_otrezok(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[(1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_pol_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[[1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[(1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_point(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_otrezok(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[(1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[[1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[(1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_point(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_interval(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[(1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_pol_interval(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[[1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[(1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_point(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_interval(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_otrezok(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[(1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_pol_interval(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[[1, 7)]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[(1, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_point(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[{11}]')
        self.assertTrue(inter1 < inter2)

    def test_pol_interval_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Intervals('[[0, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[(0, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_interval_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[[0, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_pol_otrezok_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[(0, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[(0, 7]]')
        self.assertTrue(inter1 < inter2)

    def test_point_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Intervals('[[0, 7]]')
        self.assertTrue(inter1 < inter2)

    # Interval
    # False
    def test_false_point_lt_pol_otrezok_eq_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('(0, 0]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_interval_eq_border(self):
        inter1 = interval.Interval('{0}')
        inter2 = interval.Interval('[0, 0]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Interval('{0}')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_interval_eq_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_pol_otrezok_eq_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_interval_eq_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_pol_otrezok_eq_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_interval_lt_str(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertTrue(inter1 < '(1, 7)')
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом невозможно',))
        except:
            self.assertTrue(False)

    # Interval < Intervals
    # False
    def test_false_otrezok_lt_list_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_interval(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_otrezok(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_pol_interval(self):
        inter1 = interval.Interval('[1, 7)')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_pol_otrezok(self):
        inter1 = interval.Interval('(1, 7]')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_point(self):
        inter1 = interval.Interval('{11}')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_pol_otrezok_eq_left_border(self):
        inter1 = interval.Interval('(0, 7]')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_point_lt_list_interval_eq_left_border(self):
        inter1 = interval.Interval('[0, 7]')
        inter2 = interval.Intervals('[{0}]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_interval_lt_list_interval_eq_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[[0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_otrezok_lt_list_pol_otrezok_eq_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[(0, 5)]')
        self.assertFalse(inter1 < inter2)

    def test_false_interval_lt_list_interval_eq_border(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Intervals('[[0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_false_pol_otrezok_lt_list_pol_otrezok_eq_border(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Intervals('[(0, 5]]')
        self.assertFalse(inter1 < inter2)

    def test_interval_lt_list_two_interval(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(1, 7), [9, 12]]')
            self.assertTrue(inter1 < inter2)
        except ValueError as e:
            self.assertEqual(e.args, (
                'Сравнение интервала состоящего из нескольких промежутков с интервалом из одного промежутка невозможно',))
        except:
            self.assertTrue(False)

    # Test add
    # Interval
    # True
    def test_otrezok_add_int_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + 4), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_int_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + 10), '[(0, 5), {10}]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_int_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + 0), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_int_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + 5), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_int_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + 4), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_int_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + 10), '[(0, 5], {10}]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_int_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + 0), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_int_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + 5), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_int_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + 4), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_int_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + 10), '[[0, 5], {10}]')
        except:
            self.assertFalse(True)

    def test_interval_add_int_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + 0), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_int_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + 5), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_int_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + 4), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_int_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + 10), '[[0, 5), {10}]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_int_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + 0), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_int_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + 5), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(3, 7)')
            self.assertEqual(str(inter1 + inter2), '(0, 7)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(5, 9)')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), (5, 9)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(3, 4]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(5, 9]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), (5, 9]]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(-3, 0]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('(-3, -1]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[3, 4)')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[5, 9)')
            self.assertEqual(str(inter1 + inter2), '(0, 9)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_pol_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[6, 9)')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), [6, 9)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[3, 4]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[5, 9]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[-3, 0]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('[6, 9]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), [6, 9]]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_interval_6(self):
        try:
            inter1 = interval.Interval('(12, 15)')
            inter2 = interval.Interval('[0, 15]')
            self.assertEqual(str(inter1 + inter2), '[0, 15]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_point_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('{5}')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_point_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('{4}')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_point_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('{9}')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), {9}]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_point_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('{0}')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_point_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Interval('{-3}')
            self.assertEqual(str(inter1 + inter2), '[{-3}, (0, 5)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(3, 7)')
            self.assertEqual(str(inter1 + inter2), '(0, 7)')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(6, 9)')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], (6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(-3, 4]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(5, 9]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(-3, 0]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('(-3, -1]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[3, 4)')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[5, 9)')
            self.assertEqual(str(inter1 + inter2), '(0, 9)')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_pol_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[6, 9)')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], [6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[3, 4]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[5, 9]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[-3, 0]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('[6, 9]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], [6, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_point_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('{0}')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_point_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('{4}')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_point_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('{9}')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], {9}]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_point_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Interval('{-3}')
            self.assertEqual(str(inter1 + inter2), '[{-3}, (0, 5]]')
        except:
            self.assertFalse(True)

    def test_interval_add_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(3, 7)')
            self.assertEqual(str(inter1 + inter2), '[0, 7)')
        except:
            self.assertFalse(True)

    def test_interval_add_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(5, 9)')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_interval_add_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(-3, 0)')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(3, 4]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(5, 9]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(-3, 0]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('(-3, -1]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], [0, 5]]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[3, 4)')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[5, 9)')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_pol_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[6, 9)')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], [6, 9)]')
        except:
            self.assertFalse(True)

    def test_interval_add_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[3, 4]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[5, 9]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_interval_add_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[-3, 0]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('[6, 9]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], [6, 9]]')
        except:
            self.assertFalse(True)

    def test_interval_add_point_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('{5}')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_point_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('{4}')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_point_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('{9}')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], {9}]')
        except:
            self.assertFalse(True)

    def test_interval_add_point_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('{0}')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_point_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Interval('{-3}')
            self.assertEqual(str(inter1 + inter2), '[{-3}, [0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(3, 7)')
            self.assertEqual(str(inter1 + inter2), '[0, 7)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(6, 9)')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), (6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(-3, 0)')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(-3, 4]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(5, 9]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), (5, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(-3, 0]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('(-3, -1]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], [0, 5)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[3, 4)')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[5, 9)')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_pol_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[6, 9)')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), [6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[3, 4]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[5, 9]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[-3, 0]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('[6, 9]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), [6, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_point_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('{0}')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_point_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('{4}')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_point_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('{9}')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), {9}]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_point_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Interval('{-3}')
            self.assertEqual(str(inter1 + inter2), '[{-3}, [0, 5)]')
        except:
            self.assertFalse(True)

    def test_point_add_otrezok_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_point_add_otrezok_2(self):
        try:
            inter1 = interval.Interval('{7}')
            inter2 = interval.Interval('(3, 7)')
            self.assertEqual(str(inter1 + inter2), '(3, 7]')
        except:
            self.assertFalse(True)

    def test_point_add_otrezok_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(6, 9)')
            self.assertEqual(str(inter1 + inter2), '[{0}, (6, 9)]')
        except:
            self.assertFalse(True)

    def test_point_add_otrezok_4(self):
        try:
            inter1 = interval.Interval('{5}')
            inter2 = interval.Interval('(-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), {5}]')
        except:
            self.assertFalse(True)

    def test_point_add_otrezok_5(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(-1, 6)')
            self.assertEqual(str(inter1 + inter2), '(-1, 6)')
        except:
            self.assertFalse(True)

    def test_point_add_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(-3, 4]')
            self.assertEqual(str(inter1 + inter2), '(-3, 4]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('(5, 9]')
            self.assertEqual(str(inter1 + inter2), '[{0}, (5, 9]]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Interval('(-3, 0]')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0], {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_interval_1(self):
        try:
            inter1 = interval.Interval('{5}')
            inter2 = interval.Interval('[0, 5)')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_interval_2(self):
        try:
            inter1 = interval.Interval('{3}')
            inter2 = interval.Interval('[2, 4)')
            self.assertEqual(str(inter1 + inter2), '[2, 4)')
        except:
            self.assertFalse(True)

    def test_point_add_pol_interval_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('[5, 9)')
            self.assertEqual(str(inter1 + inter2), '[{0}, [5, 9)]')
        except:
            self.assertFalse(True)

    def test_point_add_pol_interval_4(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Interval('[-3, 0)')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_interval_1(self):
        try:
            inter1 = interval.Interval('{2}')
            inter2 = interval.Interval('[0, 5]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_interval_2(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('[3, 4]')
            self.assertEqual(str(inter1 + inter2), '[{0}, [3, 4]]')
        except:
            self.assertFalse(True)

    def test_point_add_interval_3(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Interval('[5, 9]')
            self.assertEqual(str(inter1 + inter2), '[[5, 9], {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_point_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Interval('{10}')
            self.assertEqual(str(inter1 + inter2), '[{0}, {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_point_2(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Interval('{4}')
            self.assertEqual(str(inter1 + inter2), '[{4}, {10}]')
        except:
            self.assertFalse(True)

    # Interval + Intervals
    # True
    def test_otrezok_add_list_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(0, 5)]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(3, 7)]')
            self.assertEqual(str(inter1 + inter2), '(0, 7)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(5, 9)]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), (5, 9)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(0, 5]]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), (5, 9]]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(-3, -1]]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[3, 4)]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[5, 9)]')
            self.assertEqual(str(inter1 + inter2), '(0, 9)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), (0, 5)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_pol_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), [6, 9)]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[5, 9]]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[[6, 9]]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), [6, 9]]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_point_1(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[{5}]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_point_2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[{4}]')
            self.assertEqual(str(inter1 + inter2), '(0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_point_3(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[{9}]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5), {9}]')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_point_4(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[{0}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_otrezok_add_list_point_5(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[{-3}]')
            self.assertEqual(str(inter1 + inter2), '[{-3}, (0, 5)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(0, 5)]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(3, 7)]')
            self.assertEqual(str(inter1 + inter2), '(0, 7)')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], (6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(0, 5]]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(-3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(5, 9]]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[(-3, -1]]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[3, 4)]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[5, 9)]')
            self.assertEqual(str(inter1 + inter2), '(0, 9)')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), (0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_pol_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], [6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_interval_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_interval_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_interval_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[5, 9]]')
            self.assertEqual(str(inter1 + inter2), '(0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_interval_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_interval_5(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[[6, 9]]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], [6, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_point_1(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[{0}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_point_2(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[{4}]')
            self.assertEqual(str(inter1 + inter2), '(0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_point_3(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[{9}]')
            self.assertEqual(str(inter1 + inter2), '[(0, 5], {9}]')
        except:
            self.assertFalse(True)

    def test_pol_otrezok_add_list_point_4(self):
        try:
            inter1 = interval.Interval('(0, 5]')
            inter2 = interval.Intervals('[{-3}]')
            self.assertEqual(str(inter1 + inter2), '[{-3}, (0, 5]]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(3, 7)]')
            self.assertEqual(str(inter1 + inter2), '[0, 7)')
        except:
            self.assertFalse(True)

    def test_interval_add_list_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(5, 9)]')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_interval_add_list_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(3, 4]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[(-3, -1]]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], [0, 5]]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[3, 4)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[5, 9)]')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_pol_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], [6, 9)]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[3, 4]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[[6, 9]]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], [6, 9]]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_point_1(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[{5}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_point_2(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[{4}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_point_3(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[{9}]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5], {9}]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_point_4(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[{0}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_interval_add_list_point_5(self):
        try:
            inter1 = interval.Interval('[0, 5]')
            inter2 = interval.Intervals('[{-3}]')
            self.assertEqual(str(inter1 + inter2), '[{-3}, [0, 5]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(3, 7)]')
            self.assertEqual(str(inter1 + inter2), '[0, 7)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), (6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(-3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), (5, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_otrezok_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[(-3, -1]]')
            self.assertEqual(str(inter1 + inter2), '[(-3, -1], [0, 5)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[3, 4)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[5, 9)]')
            self.assertEqual(str(inter1 + inter2), '[0, 9)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_pol_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), [6, 9)]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_interval_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_interval_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[3, 4]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_interval_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[0, 9]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_interval_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '[-3, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_interval_5(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[[6, 9]]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), [6, 9]]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_point_1(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[{0}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_point_2(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[{4}]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_point_3(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[{9}]')
            self.assertEqual(str(inter1 + inter2), '[[0, 5), {9}]')
        except:
            self.assertFalse(True)

    def test_pol_interval_add_list_point_4(self):
        try:
            inter1 = interval.Interval('[0, 5)')
            inter2 = interval.Intervals('[{-3}]')
            self.assertEqual(str(inter1 + inter2), '[{-3}, [0, 5)]')
        except:
            self.assertFalse(True)

    def test_point_add_list_otrezok_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5)')
        except:
            self.assertFalse(True)

    def test_point_add_list_otrezok_2(self):
        try:
            inter1 = interval.Interval('{7}')
            inter2 = interval.Intervals('[(3, 7)]')
            self.assertEqual(str(inter1 + inter2), '(3, 7]')
        except:
            self.assertFalse(True)

    def test_point_add_list_otrezok_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(6, 9)]')
            self.assertEqual(str(inter1 + inter2), '[{0}, (6, 9)]')
        except:
            self.assertFalse(True)

    def test_point_add_list_otrezok_4(self):
        try:
            inter1 = interval.Interval('{5}')
            inter2 = interval.Intervals('[(-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0), {5}]')
        except:
            self.assertFalse(True)

    def test_point_add_list_otrezok_5(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(-1, 6)]')
            self.assertEqual(str(inter1 + inter2), '(-1, 6)')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_otrezok_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_otrezok_2(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(-3, 4]]')
            self.assertEqual(str(inter1 + inter2), '(-3, 4]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_otrezok_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[(5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[{0}, (5, 9]]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_otrezok_4(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Intervals('[(-3, 0]]')
            self.assertEqual(str(inter1 + inter2), '[(-3, 0], {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_interval_1(self):
        try:
            inter1 = interval.Interval('{5}')
            inter2 = interval.Intervals('[[0, 5)]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_interval_2(self):
        try:
            inter1 = interval.Interval('{3}')
            inter2 = interval.Intervals('[[2, 4)]')
            self.assertEqual(str(inter1 + inter2), '[2, 4)')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_interval_3(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[[5, 9)]')
            self.assertEqual(str(inter1 + inter2), '[{0}, [5, 9)]')
        except:
            self.assertFalse(True)

    def test_point_add_list_pol_interval_4(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Intervals('[[-3, 0)]')
            self.assertEqual(str(inter1 + inter2), '[[-3, 0), {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_list_interval_1(self):
        try:
            inter1 = interval.Interval('{2}')
            inter2 = interval.Intervals('[[0, 5]]')
            self.assertEqual(str(inter1 + inter2), '[0, 5]')
        except:
            self.assertFalse(True)

    def test_point_add_list_interval_2(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[[3, 4]]')
            self.assertEqual(str(inter1 + inter2), '[{0}, [3, 4]]')
        except:
            self.assertFalse(True)

    def test_point_add_list_interval_3(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Intervals('[[5, 9]]')
            self.assertEqual(str(inter1 + inter2), '[[5, 9], {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_list_point_1(self):
        try:
            inter1 = interval.Interval('{0}')
            inter2 = interval.Intervals('[{10}]')
            self.assertEqual(str(inter1 + inter2), '[{0}, {10}]')
        except:
            self.assertFalse(True)

    def test_point_add_list_point_2(self):
        try:
            inter1 = interval.Interval('{10}')
            inter2 = interval.Intervals('[{4}]')
            self.assertEqual(str(inter1 + inter2), '[{4}, {10}]')
        except:
            self.assertFalse(True)

    # Intervals
    # True
    def test_one_list_add_one_list_adds_1(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_one_list_add_one_list_union(self):
        inter1 = interval.Intervals('[0, 5)')
        inter2 = interval.Intervals('(5, 10]')
        self.assertEqual(str(inter1.__add__(inter2)), '[[0, 5), (5, 10]]')

    def test_two_list_add_two_list(self):
        inter1 = interval.Intervals('[0, 5], (15, 20]')
        inter2 = interval.Intervals('[5, 15], (18, 22]')
        self.assertEqual(str(inter1 + inter2), '[0, 22]')

    def test_one_list_add_two_list(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10], (10, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_one_list_add_two_list_union(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10], (10, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_one_list_add_one_list_1(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[10, 15]')
        self.assertEqual(str(inter1 + inter2), '[[0, 5], [10, 15]]')

    def test_one_list_add_one_list_adds_2(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[5, 15]')
        self.assertEqual(str(inter1 + inter2), '[0, 15]')

    def test_one_list_add_point(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Interval('{5}')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_one_list_add_point_union(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Interval('{15}')
        self.assertEqual(str(inter1 + inter2), '[[0, 10], {15}]')

    # TODO посмотреть точки вместе
    def test_point_add_point(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{10}')
        self.assertEqual(str(inter1 + inter2), '[{5}, {10}]')

    def test_one_list_add_point_adds(self):
        inter1 = interval.Intervals('[0, 5)')
        inter2 = interval.Interval('{5}')
        self.assertEqual(str(inter1 + inter2), '[0, 5]')

    def test_one_list_add_one_list_adds_3(self):
        inter1 = interval.Intervals('[0, 20]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_one_list_add_one_list_2(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[10, 15]')
        self.assertEqual(str(inter1 + inter2), '[[0, 5], [10, 15]]')

    def test_two_list_add_two_list_adds(self):
        inter1 = interval.Intervals('[0, 5], [10, 15]')
        inter2 = interval.Intervals('[5, 10], [12, 20]')
        self.assertEqual(str(inter1 + inter2), '[0, 20]')

    def test_one_list_otrezok_add_one_list_interval(self):
        inter1 = interval.Intervals('(0, 5)')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '(0, 10]')

    def test_one_list_add_one_list_float(self):
        inter1 = interval.Intervals('[0.0, 5.5]')
        inter2 = interval.Intervals('[5.5, 10.0]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_one_list_add_one_list_adds_4(self):
        inter1 = interval.Intervals('[0, 100]')
        inter2 = interval.Intervals('[50, 150]')
        self.assertEqual(str(inter1 + inter2), '[0, 150]')

    def test_one_list_add_one_list_adds_5(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_one_list_add_one_list_adds_6(self):
        inter1 = interval.Intervals('[0, 5]')
        inter2 = interval.Intervals('[5, 10]')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    # Interval
    # False
    def test_false_add_str(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            self.assertEqual(str(inter1 + '(1, 7)'), '[(0, 7)]')
        except TypeError as e:
            self.assertEqual(e.args, ('Добавление интервала или точки не возможно',))
        except:
            self.assertTrue(False)

    # Intervals
    # False
    def test_one_list_add_str(self):
        try:
            inter1 = interval.Intervals('[0, 5]')
            self.assertEqual(str(inter1 + '[5, 10]'), '[0, 10]')
        except TypeError as e:
            self.assertEqual(e.args, ('Добавление интервала или точки не возможно',))
        except:
            self.assertTrue(False)

    # Test in
    # Interval
    # True
    def test_point_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('{0}')
        self.assertTrue(inter2 in inter1)

    def test_point_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('{0}')
        self.assertTrue(inter2 in inter1)

    def test_point_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('{5}')
        self.assertTrue(inter2 in inter1)

    def test_point_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('{4}')
        self.assertTrue(inter2 in inter1)

    def test_int_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        self.assertTrue(3 in inter1)

    def test_int_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        self.assertTrue(3 in inter1)

    def test_int_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        self.assertTrue(3 in inter1)

    def test_int_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        self.assertTrue(3 in inter1)

    def test_pol_interval_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[0, 4)')
        self.assertTrue(inter2 in inter1)

    def test_pol_interval_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[0, 4)')
        self.assertTrue(inter2 in inter1)

    def test_pol_interval_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[2, 5)')
        self.assertTrue(inter2 in inter1)

    def test_pol_interval_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[2, 4)')
        self.assertTrue(inter2 in inter1)

    def test_interval_in_interval_1(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_interval_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_interval_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_interval_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_pol_otrezok_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_pol_otrezok_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_pol_otrezok_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_pol_otrezok_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(2, 3]')
        self.assertTrue(inter2 in inter1)

    def test_otrezok_in_interval_1(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(2, 4)')
        self.assertTrue(inter2 in inter1)

    def test_otrezok_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(2, 4)')
        self.assertTrue(inter2 in inter1)

    def test_otrezok_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(2, 4)')
        self.assertTrue(inter2 in inter1)

    def test_otrezok_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(2, 4)')
        self.assertTrue(inter2 in inter1)

    # Intervals
    # True
    def test_int_in_list_interval_1(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertTrue(5 in inter)

    def test_interval_in_list_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        sub_inter = interval.Interval('[2, 8]')
        self.assertTrue(sub_inter in inter)

    def test_int_in_list_interval_2(self):
        inter = interval.Intervals('[[0, 10], {15}]')
        self.assertTrue(15 in inter)

    def test_list_interval_in_list_interval(self):
        inter = interval.Intervals('[[0, 10], [15, 20]]')
        sub_inter = interval.Intervals('[[3, 7], [16, 18]]')
        self.assertTrue(sub_inter in inter)

    def test_start_in_list_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertTrue(0 in inter)

    def test_end_in_list_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertTrue(10 in inter)

    # Interval
    # False
    def test_false_contains_type(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = '(1, 7)'
            self.assertTrue(inter2 in inter1)
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertTrue(False)

    def test_false_point_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('{-3}')
        self.assertFalse(inter2 in inter1)

    def test_false_point_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('{-3}')
        self.assertFalse(inter2 in inter1)

    def test_false_point_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('{-3}')
        self.assertFalse(inter2 in inter1)

    def test_false_point_in_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('{-3}')
        self.assertFalse(inter2 in inter1)

    def test_false_int_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        self.assertFalse(-3 in inter1)

    def test_false_int_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        self.assertFalse(-3 in inter1)

    def test_false_int_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        self.assertFalse(-3 in inter1)

    def test_false_int_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        self.assertFalse(-3 in inter1)

    def test_false_pol_interval_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_interval_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_interval_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_interval_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_interval_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_interval_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_interval_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('[-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_interval_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_otrezok_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_otrezok_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_otrezok_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_pol_otrezok_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(-2, -1]')
        self.assertFalse(inter2 in inter1)

    def test_false_otrezok_in_interval(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('(-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_otrezok_in_pol_interval(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('(-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_otrezok_in_pol_otrezok(self):
        inter1 = interval.Interval('(0, 5]')
        inter2 = interval.Interval('(-2, -1)')
        self.assertFalse(inter2 in inter1)

    def test_false_otrezok_in_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(-2, -1)')
        self.assertFalse(inter2 in inter1)

    # Intervals
    # False
    def test_false_list_interval_in_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[(0, 5), [5, 10]]')
        self.assertFalse(inter2 in inter1)

    def test_false_int_in_list_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertFalse(15 in inter)

    def test_false_interval_in_list_interval(self):
        inter = interval.Intervals('[[0, 10]]')
        sub_inter = interval.Interval('[11, 20]')
        self.assertFalse(sub_inter in inter)

    def test_false_int_in_list_interval_before(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertFalse(-1 in inter)

    def test_false_int_in_list_interval_after(self):
        inter = interval.Intervals('[[0, 10]]')
        self.assertFalse(11 in inter)

    def test_false_list_interval_in_list_interval(self):
        inter = interval.Intervals('[[0, 10], [15, 20]]')
        sub_inter = interval.Intervals('[[12, 14]]')
        self.assertFalse(sub_inter in inter)

    def test_false_int_in_two_list_interval(self):
        inter = interval.Intervals('[[0, 10], [15, 20]]')
        self.assertFalse(12 in inter)

    # Test is_equal
    # Intervals
    # True
    def test_list_interval_equal_list_interval(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 10]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_two_list_interval_equal_two_list_interval(self):
        inter1 = interval.Intervals('[0, 5], [10, 15]')
        inter2 = interval.Intervals('[10, 15], [0, 5]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_two_list_interval_equal_list_interval(self):
        inter1 = interval.Intervals('[0, 15]')
        inter2 = interval.Intervals('[0, 10], [10, 15]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_point_equal_point(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{5}')
        self.assertTrue(inter1.is_equal(inter2))

    def test_list_interval_point_equal_point_list_interval(self):
        inter1 = interval.Intervals('[0, 5], {10}')
        inter2 = interval.Intervals('{10}, [0, 5]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_list_interval_equal_two_list_interval(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 5], [5, 10]')
        self.assertTrue(inter1.is_equal(inter2))

    # Intervals
    # False
    def test_false_list_interval_equal_list_interval(self):
        inter1 = interval.Intervals('[0, 10]')
        inter2 = interval.Intervals('[0, 11]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_false_two_list_interval_equal_two_list_interval(self):
        inter1 = interval.Intervals('[0, 5], [10, 15]')
        inter2 = interval.Intervals('[10, 15], [0, 6]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_false_two_list_interval_equal_list_interval(self):
        inter1 = interval.Intervals('[0, 15]')
        inter2 = interval.Intervals('[0, 10], [10, 13]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_false_point_equal_point(self):
        inter1 = interval.Intervals('{5}')
        inter2 = interval.Intervals('{3}')
        self.assertFalse(inter1.is_equal(inter2))

    def test_false_list_interval_point_equal_point_list_interval(self):
        inter1 = interval.Intervals('[0, 5], {10}')
        inter2 = interval.Intervals('{4}, [0, 5]')
        self.assertFalse(inter1.is_equal(inter2))

    def test_false_list_interval_equal_two_list_interval(self):
        inter1 = interval.Intervals('[0, 6]')
        inter2 = interval.Intervals('[0, 5], [5, 10]')
        self.assertFalse(inter1.is_equal(inter2))

    # Test union
    # Intervals
    # True
    def test_list_interval_union(self):
        inter = interval.Intervals('[[0, 5]]')
        self.assertEqual(str(inter.union()), '[0, 5]')

    def test_list_otrezok_union(self):
        inter = interval.Intervals('[(0, 5)]')
        self.assertEqual(str(inter.union()), '(0, 5)')

    def test_list_pol_otrezok_union(self):
        inter = interval.Intervals('[(0, 1], (1, 3], (3, 10]]')
        self.assertEqual(str(inter.union()), '(0, 10]')

    def test_list_pol_otrezok_interval_union(self):
        inter = interval.Intervals('[(0, 5], [5, 10]]')
        self.assertEqual(str(inter.union()), '(0, 10]')

    def test_two_list_interval_union(self):
        inter = interval.Intervals('[[0, 5], [6, 10]]')
        self.assertEqual(str(inter.union()), '[[0, 5], [6, 10]]')

    def test_tree_list_interval_union(self):
        inter = interval.Intervals('[[0, 5], [6, 10], [0, 15]]')
        self.assertEqual(str(inter.union()), '[0, 15]')

    def test_list_interval_all_union(self):
        inter = interval.Intervals('[[0, 15], (0, 7], [6, 10], (12, 15)]')
        self.assertEqual(str(inter.union()), '[0, 15]')

    def test_list_interval_point_union(self):
        inter = interval.Intervals('[[0, 5), (5, 10], {10}]')
        self.assertEqual(str(inter.union()), '[[0, 5), (5, 10]]')

    def test_list_interval_points_union(self):
        inter = interval.Intervals('[(0, 1), (1, 7), (7, 10], {0, 1, 7}]')
        self.assertEqual(str(inter.union()), '[0, 10]')

    def test_list_interval_all_point_union(self):
        inter = interval.Intervals('[(0, 1), [5, 10], [0, 20), (1, 7), {1}')
        self.assertEqual(str(inter.union()), '[0, 20)')

    # Test in example
    def test_one_example(self):
        inter1 = interval.Intervals('[(0, 1), (1, 7), (7, 10]]')
        inter2 = interval.Intervals('{0, 1, 7}')
        self.assertEqual(str(inter1 + inter2), '[0, 10]')

    def test_two_example(self):
        inter1 = interval.Intervals('[5, 6]')
        inter2 = interval.Intervals('(-2, 4)')
        self.assertEqual(str(inter1 + inter2), '[(-2, 4), [5, 6]]')

    def test_tree_example(self):
        inter1 = interval.Intervals('(0, 12)')
        inter2 = interval.Intervals('[(-2, 1), (7, 10]]')
        self.assertEqual(str(inter1 + inter2), '(-2, 12)')

    def test_four_example(self):
        inter1 = interval.Intervals('(1, 5), (5, 7), [5, 5], [7, 7]')
        self.assertEqual(str(inter1.union()), '(1, 7]')

    def test_five_example(self):
        inter1 = interval.Intervals('{1, 3, 7}')
        inter2 = interval.Intervals('(0, 1)')
        self.assertEqual(str(inter1 + inter2), '[(0, 1], {3}, {7}]')

    # Test after prosent
    def test_float_point_to_str(self):
        inter = interval.Interval('{1.1}')
        self.assertEqual(inter.__str__(), '{1.1}')

    def test_point_add_int_1(self):
        inter1 = interval.Interval('{5}')
        self.assertEqual(str(inter1 + 5), '{5}')

    def test_false_empty_second_number(self):
        try:
            inter1 = interval.Interval('[5, a]')
            self.assertFalse(True)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали второе число для интервала',))
        except:
            self.assertFalse(True)

    def test_interval_add_point(self):
        inter1 = interval.Interval('[5, 7]')
        inter2 = interval.Interval('{5}')
        self.assertEqual(str(inter2 + inter1), '[5, 7]')

    def test_otrezok_in_interval_2(self):
        inter1 = interval.Interval('[5, 5]')
        inter2 = interval.Interval('(5, 5)')
        self.assertTrue(inter2 in inter1)

    def test_interval_in_interval_2(self):
        inter1 = interval.Interval('[5, 5]')
        inter2 = interval.Interval('[5, 5]')
        self.assertTrue(inter2 in inter1)

    def test_point_in_point(self):
        inter1 = interval.Interval('{5}')
        inter2 = interval.Interval('{5}')
        self.assertTrue(inter2 in inter1)

    def test_false_point_in_point(self):
        inter1 = interval.Interval('{5}')
        inter2 = interval.Interval('{4}')
        self.assertFalse(inter2 in inter1)

    def test_create_list_interval_forgot_brackets(self):
        try:
            inter = interval.Intervals('[(12, 20')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы забыли закрывающую скобку ), ] или }',))
        except:
            self.assertTrue(False)

    def test_list_interval_add_int(self):
        inter1 = interval.Intervals('[5, 8]')
        self.assertEqual(str(inter1 + 9), '[[5, 8], {9}]')

    def test_false_list_interval_equal_str(self):
        other = 'as'
        try:
            inter1 = interval.Intervals('[5, 8]')
            self.assertFalse(inter1.is_equal(other))
        except TypeError as e:
            self.assertEqual(e.args, ('Не возможно проверить на эквивалентность интервала с ' + str(type(other)), ))
        except:
            self.assertFalse(True)

    def test_list_interval_equal_interval(self):
        inter1 = interval.Intervals('[5, 8]')
        inter2 = interval.Interval('[5, 8]')
        self.assertTrue(inter1.is_equal(inter2))

    def test_false_str_in_list_interval(self):
        try:
            inter1 = interval.Intervals('[5, 8]')
            self.assertTrue('8' in inter1)
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом не возможно',))
        except:
            self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
    """
    После проверки работы всех тестов, необходимо проверить процент проверки кода, для этого необходимо сделать следующие команды:
    pip install coverage - для установки пакета (только один раз)
    python -m coverage run -m unittest - фиксация прохождения тестов
    python -m coverage report - сбор информации о прохождении тестов по коду
    python -m coverage html - отображение в читаемом виде (html)
    Далее в папке htmlcov открыть файл index.html в браузере и проанализировать полученный результат
    """
