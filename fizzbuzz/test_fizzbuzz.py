import unittest
from fizzbuzz import es_multiplo

class Testfizzbuzz(unittest.TestCase):
    def test_multiplo_5(self):
        self.assertEqual(es_multiplo(10),"buzz")

if __name__ == '__main__':
    unittest.main()