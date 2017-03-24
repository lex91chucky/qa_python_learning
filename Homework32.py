import unittest
from Task3 import distance

class DistanceTests(unittest.TestCase) :
    def test_zero(self):
        res = distance(0,0,0,0)
        self.assertEqual(res, 0)
    def test_one(self):
        res = distance(-1, -1, 0.000000000000000000000001, 0)
        self.assertNotEquals(res, 0)
    def test_x(self):
        res = distance(0, 1, 2, 3)
        self.assertEqual(res, 2**0.5)

from Task24 import is_year_leap

class Is_Year_LeapTests(unittest.TestCase) :
    def test1(self):
        res = is_year_leap(2016)
        self.assertTrue(res)
    def test2(self):
        res = is_year_leap(2000)
        self.assertFalse(res)
    def test3(self):
        res = is_year_leap(1999)
        self.assertFalse(res)

from Task5 import triangle

class TriangleTests(unittest.TestCase):
    def test_1(self):
        res = triangle(2, 3, 4)
        self.assertTrue(res)


    def test_2(self):
        res = triangle(-2, -4, -3)
        self.assertFalse(res)


    def test_3(self):
        res = triangle(0, 0, 0)
        self.assertFalse(res)


    def test_4(self):
        res = triangle(8, 8, 8)
        self.assertTrue(res)

if __name__=="__main__":
    unittest.main()
