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
            self.assertEqual(e.args, ('Вы не передали число для интервала',))
        except:
            self.assertTrue(False)

    def test_false_create_interval_a(self):
        try:
            inter = interval.Interval('(10, a')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы не передали число для интервала',))
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

    # TODO Intervals
    # False
    def test_false_create_empty_list(self):
        try:
            inter = interval.Intervals('[]')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e.args, ('Вы передали пустой список интервалов',))
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

    def test_point_to_str(self):
        inter = interval.Interval('{11}')
        self.assertEqual(inter.__str__(), '{11}')

    # TODO Intervals
    # True
    def test_intervals_to_str(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.__str__(), '[0, 11]')

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

    # TODO Intervals
    # True
    def test_intervals_to_repr(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.__repr__(), '[0, 11]')

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

    # TODO Intervals
    # True
    def test_weight_intervals(self):
        inter = interval.Intervals('[[0, 11]]')
        self.assertEqual(inter.weight(), 11)

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
            self.assertEqual(e.args, ('Сравнение интервала состоящего из нескольких промежутков с интервалом из одного промежутка невозможно',))
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

    # TODO Intervals
    # True
    # False

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

    def test_interval_in_interval(self):
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

    def test_otrezok_in_interval(self):
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


    # TODO Intervals
    # True


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
        self.assertTrue(inter2 in inter1)

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


    # TODO Intervals
    # False
    def test_false_contains_intervals(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[(0, 5), [5, 10]]')
        self.assertFalse(inter2 in inter1)


if __name__ == '__main__':
    unittest.main()
