import unittest
from funciones import es_par


class TestParImpar(unittest.TestCase):

    def test_par(self):
        self.assertEqual(es_par(8), "es par")

    def test_impar(self):
        self.assertEqual(es_par(9), "es impar")

    def test_cero(self):
        self.assertEqual(es_par(0), "Es Cero")


if __name__ == '__main__':
    unittest.main()