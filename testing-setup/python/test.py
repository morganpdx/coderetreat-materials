import unittest

class TestStringMethods(unittest.TestCase):

    def test_string_compare(self):
        a = 'a string'
        b = 'another string'
        self.assertEqual(a,b)

if __name__ == '__main__':
    unittest.main()