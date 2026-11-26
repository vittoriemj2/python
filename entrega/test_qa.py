import unittest                           # librería de testing de Python
from entrega import fizzbuzz              # trae la función desde entrega.py

class TestQA(unittest.TestCase):          # al heredar de TestCase, unittest sabe que acá hay tests
   
    def test_multiplo_3(self):            # los métodos deben empezar con "test_"
        self.assertEqual(fizzbuzz(9), "Fizz")        # criterio 1: assertEqual(resultado real, esperado)
    
    def test_multiplo_5(self):
        self.assertEqual(fizzbuzz(10), "Buzz")       # criterio 2
   
    def test_multiplo_ambos(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")   # criterio 3 (B mayúscula: Python distingue)
    
    def test_0(self):
        self.assertEqual(fizzbuzz(0), 0)             # criterio 4: el 0 devuelve 0
   
    def test_devolver_numero(self):
        self.assertEqual(fizzbuzz(43), 43)           # criterio 5: 43 no es múltiplo de 3 ni de 5


if __name__ == '__main__':                # solo se cumple si corrés este archivo directamente
    unittest.main()                       # ejecuta todos los tests de la clase