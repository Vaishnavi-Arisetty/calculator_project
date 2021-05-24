import unittest
from calculatorclass import Calculator
import math as m

Ca11 = Calculator(9, 10)
Ca12 = Calculator(-9, 10)
Ca13 = Calculator(9, 0)
Ca14 = Calculator(-9, -10)
Ca21 = Calculator(9)
Ca22 = Calculator(0)
Ca23 = Calculator(10)
Ca24 = Calculator(-9)


class TestCalculator(unittest.TestCase):
    def test_object(self):
        self.assertIsInstance(Ca11, Calculator, "Not an instance")
        self.assertIsInstance(Ca12, Calculator, "Not an instance")
        self.assertIsInstance(Ca13, Calculator, "Not an instance")
        self.assertIsInstance(Ca14, Calculator, "Not an instance")
        self.assertIsInstance(Ca21, Calculator, "Not an instance")
        self.assertIsInstance(Ca22, Calculator, "Not an instance")
        self.assertIsInstance(Ca23, Calculator, "Not an instance")
        self.assertIsInstance(Ca24, Calculator, "Not an instance")

    def test_addition(self):
        self.assertEqual(Ca11.add(), 19, "Not Successful")
        self.assertEqual(Ca12.add(), 1, "Not Successful")
        self.assertEqual(Ca14.add(), -19, "Not Successful")

    def test_subtraction(self):
        self.assertEqual(Ca11.sub(), -1, "Not Successful")
        self.assertEqual(Ca12.sub(), -19, "Not Successful")
        self.assertEqual(Ca14.sub(), 1, "Not Successful")

    def test_multiply(self):
        self.assertEqual(Ca11.multiply(), 90, "Not Successful")
        self.assertEqual(Ca12.multiply(), -90, "Not Successful")
        self.assertEqual(Ca14.multiply(), 90, "Not Successful")

    def test_division(self):
        self.assertEqual(Ca11.divide(), 0.9, "Not Successful")
        self.assertEqual(Ca12.divide(), -0.9, "Not Successful")
        self.assertEqual(Ca14.divide(), 0.9, "Not Successful")
        self.assertRaises(ZeroDivisionError, Ca13.divide)

    def test_square(self):
        self.assertEqual(Ca21.square(), 81, "Not Successful")
        self.assertEqual(Ca22.square(), 0, "Not Successful")

    def test_square_root(self):
        self.assertEqual(Ca21.square_root(), 3, "Not Successful")
        self.assertRaises(ValueError, Ca24.square_root)

    def test_sine(self):
        self.assertAlmostEqual(Ca22.sine(), 0)

    def test_cosine(self):
        self.assertAlmostEqual(Ca22.cosine(), 1)

    def test_tangent(self):
        self.assertAlmostEqual(Ca22.tangent(), 0)

    def test_logarithm(self):
        self.assertEqual(Ca23.logarithm(), 1, "Not Successful")
        self.assertRaises(ValueError, Ca24.logarithm)

    def test_reciprocal(self):
        self.assertEqual(Ca23.reciprocal(), 0.1, "Not Successful")
        self.assertRaises(ZeroDivisionError, Ca22.reciprocal)


if __name__ == '__main__':
    unittest.main()
