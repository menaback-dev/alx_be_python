import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        """Test normal addition operations."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    
    def test_subtraction(self):
        """Test subtraction operations."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-10, -5), -5)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    
    def test_multiplication(self):
        """Test multiplication operations."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    
    def test_division(self):
        """Test normal division operations."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(-15, 3), -5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        """Test dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()
