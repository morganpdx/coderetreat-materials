import unittest
from fizzbuzz import *

class fizzbuzztest (unittest.TestCase):
    def test_calculate_returns_1_with_1(self):
        result = calculate(1)
        self.assertEquals(result, '1')

    def test_calculate_returns_2_with_2(self):
        result = calculate(2)
        self.assertEquals(result, '2')

    def test_calculate_returns_fizz_with_multiple_of_3(self):
        self.assertEquals(calculate(3), 'fizz')

    def test_calculate_returns_buzz_with_multiples_of_5(self):
        self.assertEquals(calculate(5), 'buzz')

    def test_calcualte_returns_fizzbuzz_with_multiples_of_15(self):
        self.assertEquals(calculate(15), 'fizzbuzz')

    def test_result_for_zero(self):
        result = calculate(0)
        self.assertEquals(result, '0')

    def test_result_for_neg_one(self):
        result = calculate(-1)
        self.assertEquals(result, '-1')

    def test_result_for_neg_3(self):
        result = calculate(-3)
        self.assertEqual(result, 'fizz')

