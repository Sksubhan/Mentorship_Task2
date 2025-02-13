import unittest
from summation import summation
class Add(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(summation(2,3),5)

    def test_negative_numbers(self):
        self.assertEqual(summation(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(summation(-2, 3), 1)

    def test_with_zero(self):
        self.assertEqual(summation(0, 5), 5)
        self.assertEqual(summation(5, 0), 5)

    def test_float_numbers(self):
        self.assertAlmostEqual(summation(2.5, 3.2), 5.7)

    def test_string_input_right(self):
        self.assertEqual(summation('Hello', -3),'Please do not use string as input')

    def test_string_input_left(self):
        self.assertEqual(summation(90, 'Hello'),'Please do not use string as input')

    def test_string_inputs(self):
        self.assertEqual(summation('Hi', 'Hello'),'Please do not use string as input')


if __name__=='__main__':
    unittest.main()
