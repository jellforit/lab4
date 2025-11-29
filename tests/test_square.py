import unittest
from geometric_lib.square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-5), 25)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area("abc")


    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5), -20)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter(None)