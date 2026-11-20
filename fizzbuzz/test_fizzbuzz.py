import unittest
from fizzbuzz import es_multiplo

class Testfizzbuzz(unittest.TestCase):
    def test_multiplo_5(self):
        self.assertEqual(es_multiplo(10), "buzz")
    def test_multiplo_3(self):
    		self.assertEqual(es_multiplo(9), "fizz")
    def test_no_aplica_multiplo_5(self):
        self.assertEqual(es_multiplo(10), 8)
    def test_devolver_numero(self):
        self.assertEqual(es_multiplo(77),77)
    def test_multiplo_ambos(self):
        self.assertEual(es_multiplo(15),"fizzbuzz")

if __name__ == '__main__':
    unittest.main()

