import unittest
from day_ten import *

class DayTenCase(unittest.TestCase):
    def test_delta(self):
        first = 4
        second = 5
        expected = second-first
        result = delta(first=first, second=second)
        self.assertEqual(expected, result)

    def test_highest_joltage(self):
        joltage_list = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        expected = 49
        result = highest_joltage_in_list(joltage_list=joltage_list)
        self.assertEqual(expected, result)

    def test_calculate_joltage_differences_first_example(self):
        joltage_list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        expected = {"1": 7, "3": 5}
        result = get_number_of_joltage_differences(joltage_list=joltage_list)
        self.assertDictEqual(expected, result)

    def test_calculate_joltage_differences_second(self):
        joltage_list = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        expected = {"1": 22, "3": 10}
        result = get_number_of_joltage_differences(joltage_list=joltage_list)
        self.assertDictEqual(expected, result)

    def test_count_distinct_adapter_paths_first_example(self):
        joltage_list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        expected = 8
        result = count_distinct_adapter_paths(joltage_list=joltage_list)
        self.assertDictEqual(expected, result)

    def test_count_distinct_adapter_paths_second(self):
        joltage_list = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        expected = 19208
        result = count_distinct_adapter_paths(joltage_list=joltage_list)
        self.assertDictEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
