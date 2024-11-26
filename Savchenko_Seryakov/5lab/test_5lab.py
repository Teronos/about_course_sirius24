import unittest
import interval

class TestInterval(unittest.TestCase):

    # Test on create and parser
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

    # Test interval to str
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

    # Test interval to repr
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

    # Test weight
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

    # Test ==
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

    # False
    def test_otrezok_eq_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('(0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_otrezok_eq_pol_otrezok(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_otrezok_eq_pol_interval(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_otrezok_eq_point(self):
        inter1 = interval.Interval('[0, 11]')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    def test_interval_eq_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('[0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_interval_eq_pol_otrezok(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('(0, 11]')
        self.assertFalse(inter1 == inter2)

    def test_interval_eq_pol_interval(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('[0, 11)')
        self.assertFalse(inter1 == inter2)

    def test_interval_eq_point(self):
        inter1 = interval.Interval('(0, 11)')
        inter2 = interval.Interval('{11}')
        self.assertFalse(inter1 == inter2)

    # Test <
    # True
    def test_interval_and_interval(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('(1, 7)')
        self.assertTrue(inter1 < inter2)

    def test_interval_and_otrezok(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_and_otrezok(self):
        inter1 = interval.Interval('[0, 5]')
        inter2 = interval.Interval('[1, 7]')
        self.assertTrue(inter1 < inter2)

    def test_otrezok_and_otrezok_eq_l_border(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[0, 7]')
        self.assertTrue(inter1 < inter2)

    # TODO добавить тесты, когда один из интервалов одинарный интервалс
    def test_interval_and_intervals(self):
        inter1 = interval.Interval('(0, 5)')
        inter2 = interval.Intervals('[[1, 7]]')
        self.assertTrue(inter1 < inter2)

    # False
    def test_interval_and_interval(self):
        inter1 = interval.Interval('(1, 7)')
        inter2 = interval.Interval('(0, 5)')
        self.assertFalse(inter1 < inter2)

    def test_otrezok_and_otrezok_eq_l_border(self):
        inter1 = interval.Interval('[1, 7]')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_otrezok_and_otrezok_eq_l_border(self):
        inter1 = interval.Interval('[0, 7)')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_otrezok_and_otrezok_eq(self):
        inter1 = interval.Interval('[0, 5)')
        inter2 = interval.Interval('[0, 5]')
        self.assertFalse(inter1 < inter2)

    def test_interval_and_intervals2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = '(1, 7)'
            self.assertTrue(inter1 < inter2)
        except TypeError as e:
            self.assertEqual(e.args, ('Сравнение интервала не с интервалом невозможно',))
        except:
            self.assertTrue(False)

    # TODO добавить тесты, когда один из интервалов одинарный интервалс
    def test_interval_and_intervals2(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = interval.Intervals('[(1, 7), [9, 12]]')
            self.assertTrue(inter1 < inter2)
        except ValueError as e:
            self.assertEqual(e.args, ('Сравнение интервала состоящего из нескольких промежутков с интервалом из одного промежутка невозможно',))
        except:
            self.assertTrue(False)



    # Test +
    # True
    # def test_int_to_point(self):
    #     try:
    #         inter1 = interval.Interval('(0, 5)')
    #         inter2 = 4
    #     self.assert

    # False
    def test_false_add_type(self):
        try:
            inter1 = interval.Interval('(0, 5)')
            inter2 = '(1, 7)'
            self.assertTrue(inter1 + inter2)
        except TypeError as e:
            self.assertEqual(e.args, ('Добавление интервала или точки не возможно',))
        except:
            self.assertTrue(False)


    # Test in
    # True


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

    # TODO Intervals
    # def test_false_contains_intervals(self):
    #     inter1 = interval.Interval('(0, 5)')
    #     inter2 = interval.Intervals('[(0, 5), [5, 10]]')
    #     self.assertFalse(inter2 in inter1)



    """
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """

if __name__ == '__main__':
    unittest.main()
