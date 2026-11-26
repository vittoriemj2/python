import unittest

from fizzbuzz import fizzbuzz


class TestQA(unittest.TestCase):
    # Criterio 1: múltiplo de 3 (y no de 5) -> "Fizz"
    def test_multiplo_de_3_devuelve_fizz(self):
        for n in (3, 6, 9, 12, 18, 21):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "Fizz")

    # Criterio 2: múltiplo de 5 (y no de 3) -> "Buzz"
    def test_multiplo_de_5_devuelve_buzz(self):
        for n in (5, 10, 20, 25, 35):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "Buzz")

    # Criterio 3: múltiplo de 3 y de 5 -> "FizzBuzz"
    def test_multiplo_de_3_y_5_devuelve_fizzbuzz(self):
        for n in (15, 30, 45, 60, 90):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "FizzBuzz")

    # Criterio 4: cualquier otro número -> el mismo número
    def test_otro_numero_devuelve_el_numero(self):
        for n in (1, 2, 4, 7, 8, 11, 13, 14):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), n)

    # Criterio 5: el 0 es múltiplo de 3 y de 5 -> "FizzBuzz"
    def test_cero_devuelve_fizzbuzz(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()