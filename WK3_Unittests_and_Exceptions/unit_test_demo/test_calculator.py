import unittest

from WK3_Unittests_and_Exceptions.unit_test_demo.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(3, 2)

    @unittest.skip("demonstrating skipping")
    def test_add(self):
        self.assertEqual(5, self.calculator.add())
        self.assertNotEqual(3, self.calculator.add())

    def test_minus(self):
        self.assertEqual(1, self.calculator.minus())

    def test_multiply(self):
        self.assertEqual(6, self.calculator.multiply())

    def test_divide(self):
        # self.assertEqual(2, self.calculator.divide())
        self.assertEqual(1.5, self.calculator.divide())


if __name__ == '__main__':
    unittest.main()
