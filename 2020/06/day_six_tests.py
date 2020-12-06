import unittest
from day_six import count_all_answers_in_group


class DaySixTests(unittest.TestCase):
    def test_count_all_answers_in_group_abc(self):
        group_answer = "abc"
        expected = 3
        result = count_all_answers_in_group(group_answer=group_answer)
        self.assertEqual(expected, result)


    def test_count_all_answers_in_group_abc_new_line(self):
        group_answer = "a\nb\nc"
        expected = 3
        result = count_all_answers_in_group(group_answer=group_answer)
        self.assertEqual(expected, result)


    def test_count_all_answers_in_group_acab(self):
        group_answer = "ab\nac"
        expected = 3
        result = count_all_answers_in_group(group_answer=group_answer)
        self.assertEqual(expected, result)


    def test_count_all_answers_in_group_aaaa(self):
        group_answer = "a\na\na\na"
        expected = 1
        result = count_all_answers_in_group(group_answer=group_answer)
        self.assertEqual(expected, result)


    def test_count_all_answers_in_group_b(self):
        group_answer = "b"
        expected = 1
        result = count_all_answers_in_group(group_answer=group_answer)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
