import unittest
import interval

class TestInterval(unittest.TestCase):

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

    def test_false_create_point(self):
        try:
            inter = interval.Interval('10}')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'В вашем интервале не хватает открывающей скобки [, ( или {')
        except:
            self.assertTrue(False)

    def test_false_create(self):
        try:
            inter = interval.Interval('')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'Вы передали пустой интервал')
        except:
            self.assertTrue(False)

    def test_false_create_a(self):
        try:
            inter = interval.Interval('(a')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'Вы не передали число для интервала')
        except:
            self.assertTrue(False)

    def test_false_create_pol_interval(self):
        try:
            inter = interval.Interval('(10, ')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'Вы не передали число для интервала')
        except:
            self.assertTrue(False)

    def test_false_create_interval_a(self):
        try:
            inter = interval.Interval('(10, a')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'Вы не передали второе число для интервала')
        except:
            self.assertTrue(False)

    def test_false_create_interval(self):
        try:
            inter = interval.Interval('(10, 11')
            self.assertTrue(False)
        except ValueError as e:
            self.assertEqual(e, 'В вашем интервале не хватает закрывающей скобки ], ) или }')
        except:
            self.assertTrue(False)

    def test_false_create_invert_interval(self):
        try:
            inter = interval.Interval('[100, 11]')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

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
