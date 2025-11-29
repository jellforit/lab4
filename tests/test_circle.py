import unittest
import math
from geometric_lib.circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        self.assertAlmostEqual(area(-5), math.pi * 25)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area("hello")


    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        self.assertAlmostEqual(perimeter(-5), -10 * math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter(None)