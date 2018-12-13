import unittest
from ThirdDay import *

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.sut = ThirdDay()

    def test_createCoordinatesSingle(self):

        x = 0
        y = 0
        width = 1
        height = 1

        expected = {"0,0"}
        result = self.sut.createCoordinates(x, y, width, height)

        self.assertEqual(expected, result)

    def test_createCoordinatesMultiple(self):
        x = 2
        y = 2
        width = 2
        height = 2

        expected = {"2,2", "2,3", "3,2", "3,3"}
        result = self.sut.createCoordinates(x, y, width, height)

        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
