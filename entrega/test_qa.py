import unittest                    # librería de testing que viene con Python

from entrega import fizzbuzz       # importa la función desde entrega.py (mismo nombre de archivo)


class TestQA(unittest.TestCase):   # al heredar de TestCase, unittest sabe que acá hay tests

    # Criterio 1: múltiplo de 3 (y no de 5) -> "Fizz"

    def test_multiplo_de_3_devuelve_fizz(self):   # los métodos DEBEN empezar con "test_"
        for n in (3, 6, 9, 12, 18, 21):           # probamos varios números, no solo uno
            with self.subTest(n=n):               # si uno falla, el informe dice cuál (n=...)
                self.assertEqual(fizzbuzz(n), "Fizz")   # compara resultado real vs esperado

    
    # Criterio 2: múltiplo de 5 (y no de 3) -> "Buzz"
    def test_multiplo_de_5_devuelve_buzz(self):
        for n in (5, 10, 20, 25, 35):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "Buzz")

    
    # Criterio 3: múltiplo de 3 y de 5 a la vez -> "FizzBuzz" (el que fallaba con la función original)
    def test_multiplo_de_3_y_5_devuelve_fizzbuzz(self):
        for n in (15, 30, 45, 60, 90):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "FizzBuzz")

   
    # Criterio 4: cualquier otro número -> devuelve el mismo número
    def test_otro_numero_devuelve_el_numero(self):
        for n in (1, 2, 4, 7, 8, 11, 13, 14):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), n)

    
    # Criterio 5: caso borde, el 0 es múltiplo de 3 y de 5 -> "FizzBuzz"
    def test_cero_devuelve_fizzbuzz(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")


if __name__ == "__main__":         # solo se cumple si corrés este archivo directamente
    unittest.main()                # ejecuta todos los tests de la clase