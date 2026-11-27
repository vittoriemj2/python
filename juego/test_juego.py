import unittest
from juego import juego

class Test_juego(unittest.TestCase):
    def test_devuelve_15(self):
        esperado = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
                    11, "Fizz", 13, 14, "FizzBuzz"]
        self.assertEqual(juego(15), esperado)
    def test_devuelve_1(self):
        self.assertEqual(juego(1), [1])
    def test_devuelve_0(self):
        self.assertEqual(juego(0), [])

if __name__ == '__main__':
    unittest.main()
     