import unittest
import math
from geometry import square_area, square_perimeter, rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestCalculator(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square_area(3), 9)
        self.assertEqual(square_area(-1), 1)
        self.assertEqual(square_area(0), 0)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimer(-1), -4)
        self.assertEqual(square_perimeter(0), 0)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(-1, 1), -1)
        self.assertEqual(rectangle_area(10, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10)
        self.assertEqual(rectangle_perimeter(-1, 1), 0)
        self.assertEqual(rectangle_perimeter(10, 0), 20)
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_circle_area(self):
        self.assertEqual(circle_area(2), 4 * math.pi)
        self.assertEqual(circle_area(-3), 9 * math.pi)
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(0), 0)

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(2), 4 * math.pi)
        self.assertEqual(circle_circumference(-3), -6 * math.pi)
        self.assertEqual(circle_circumference(1), 2 * math.pi)
        self.assertEqual(circle_circumference(0), 0)

if __name__ == '__main__':
    unittest.main()
