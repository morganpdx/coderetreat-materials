import unittest
from fizzbuzz import *

class FizzBuzzTest(unittest.TestCase):

    def test_result_for_1(self):
        result = calculate(1)
        self.assertEquals(result, '1')

    def test_result_for_2(self):
        result = calculate(2)
        self.assertEquals(result, '2')

    def test_result_for_multiple_of_3(self):
        result = calculate(3)
        self.assertEquals(result, 'fizz')

        result = calculate(6)
        self.assertEquals(result, 'fizz')

    def test_result_for_multiple_of_5(self):
        result = calculate(5)
        self.assertEquals(result, 'buzz')

    def test_result_for_multiple_of_15(self):
        result = calculate(15)
        self.assertEquals(result, 'fizzbuzz')

    def test_result_for_zero(self):
        result = calculate(0)
        self.assertEquals(result, '0')

    def test_result_for_neg_one(self):
        result = calculate(-1)
        self.assertEquals(result, '-1')

    def test_result_for_neg_3(self):
        result = calculate(-3)
        self.assertEqual(result, 'fizz')

    def test_final_output(self):
        result = output_list()
        expected = ' 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz'
        self.assertEquals(result, expected)

