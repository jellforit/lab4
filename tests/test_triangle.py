import unittest
from geometric_lib.triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-10, 5), -25)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 5.0)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area("a", 5)
        with self.assertRaises(TypeError):
            area(10, "b")

            
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 4, 5), 9)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-3, 4, 5), 6)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter("a", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "b", 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, "c")