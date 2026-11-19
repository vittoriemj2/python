import unittest

class Testfizzbuzz(unittest.TestCase):
	def test_multiplo_5(self):
  	    self.assertEqual(fizzbuzz(10),"buzz")

if __name__ == '__main__':
    unittest.main()