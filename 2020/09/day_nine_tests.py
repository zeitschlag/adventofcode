import unittest
from day_nine import *

class DayNineCase(unittest.TestCase):
    def test_preamble_offset_3(self):
        code = [1,2,3,4,5,6,7,8]
        offset = 0
        length = 3
        expected = [1,2,3]
        result = preamble(code=code, offset=offset, length=length)
        self.assertListEqual(expected, result)

    def test_is_number_valid_26(self):
        number = 26
        code_list = [*range(1, 26)]
        expected = True
        result = is_number_valid(number=number, code_list=code_list)
        self.assertEqual(expected, result)

    def test_is_number_valid_49(self):
        number = 49
        code_list = [*range(1, 26)]
        expected = True
        result = is_number_valid(number=number, code_list=code_list)
        self.assertEqual(expected, result)

    def test_is_number_valid_100(self):
        number = 100
        code_list = [*range(1, 26)]
        expected = False
        result = is_number_valid(number=number, code_list=code_list)
        self.assertEqual(expected, result)

    def test_first_part(self):
        filename = "sample_input.txt"
        expected = 127
        length = 5
        result = find_first_invalid_number(filename=filename, length=length)
        self.assertEqual(expected, result)

    def test_second_part(self):
        filename = "sample_input.txt"
        expected = 62
        length = 5
        result = second_part(filename=filename, length=length)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
