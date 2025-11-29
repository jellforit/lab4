import unittest
from geometric_lib.rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(5, 0), 0)

    def test_area_negative(self):
        self.assertEqual(area(-5, 10), -50)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area(10, None)

        with self.assertRaises(TypeError):
            area(None, 10)

        with self.assertRaises(TypeError):
            area(5, {"a": 1})


    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 10), 20)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5, 10), 10)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5, 4.0), 13.0)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter("qwe", 10)
        with self.assertRaises(TypeError):
            perimeter(10, None)