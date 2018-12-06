import unittest
from second_day import *

class SecondDayTests(unittest.TestCase):

    def setUp(self):
        self.sut = SecondDay()

    def test_checkCharacterInStringTwice(self):
        input = "aabcd"
        result = self.sut.containsRandomCharacterExactlyTwice(input)
        
        self.assertTrue(result)

    def test_checkCharacterInStringTwiceFalse(self):
        input = "abcde"
        result = self.sut.containsRandomCharacterExactlyTwice(input)

        self.assertFalse(result)

    def test_checkCharacterInStringTwiceThreeTimes(self):
        input = "aaabcde"
        result = self.sut.containsRandomCharacterExactlyTwice(input)

        self.assertFalse(result)

    def test_checkCharacterInStringThreeTimes(self):
        input = "aaabcd"
        result = self.sut.containsRandomCharacterExactlyThreeTimes(input)
        
        self.assertTrue(result)

    def test_checkCharacterInStringThreeTimesFalse(self):
        input = "abcde"
        result = self.sut.containsRandomCharacterExactlyThreeTimes(input)

        self.assertFalse(result)

    def test_CheckCharacterInStringThreeTimesTwice(self):
        input = "aabcde"
        result = self.sut.containsRandomCharacterExactlyThreeTimes(input)

        self.assertFalse(result)

    def test_calculateChecksum(self):
        twosCounter = 3
        threesCounter = 4

        expected = 12
        result = self.sut.calculateChecksum(twosCounter=twosCounter, threesCounter=threesCounter)

        self.assertEqual(expected, result)

    def test_calculateChecksumZero(self):
        twos = 0
        threes = 100

        expected = 0
        result = self.sut.calculateChecksum(twosCounter=twos, threesCounter=threes)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
