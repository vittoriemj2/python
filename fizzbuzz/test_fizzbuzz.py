import unittest
from fizzbuzz import es_multiplo

class Testfizzbuzz(unittest.TestCase):
    def test_multiplo_5(self):
        self.assertEqual(es_multiplo(10), "buzz")
    def test_multiplo_3(self):
    		self.assertEqual(es_multiplo(9), "fizz")

if __name__ == '__main__':
    unittest.main()