import unittest
from day_eight import *


class DayEightTests(unittest.TestCase):
    def test_operation_nop(self):
        instruction = "nop +0"
        expected = "nop"
        result = get_operation(instruction=instruction)

        self.assertEqual(expected, result)

    def test_operation_acc(self):
        instruction = "acc +1"
        expected = "acc"
        result = get_operation(instruction=instruction)

        self.assertEqual(expected, result)

    def test_argument_99(self):
        instruction = "acc -99"
        expected = -99
        result = get_argument(instruction=instruction)

        self.assertEqual(expected, result)

    def test_argument_4(self):
        instruction = "jmp +4"
        expected = 4
        result = get_argument(instruction=instruction)

        self.assertEqual(expected, result)

    def test_run_nop(self):
        operation = "nop"
        argument = 0
        original_accumulator = 5

        expected = 1
        result = run(operation=operation, argument=argument, accumulator=original_accumulator)

        self.assertEqual(expected, result[0])
        self.assertEqual(original_accumulator, result[1])

    def test_run_acc(self):
        operation = "acc"
        argument = 13
        accumulator = 5

        expected = 1
        result = run(operation=operation, argument=argument, accumulator=accumulator)

        self.assertEqual(expected, result[0])
        self.assertEqual(accumulator+argument, result[1])

    def test_run_jmp(self):
        operation = "jmp"
        argument = 13
        original_accumulator = 5
        accumulator = original_accumulator

        expected = 13
        result = run(operation=operation, argument=argument, accumulator=accumulator)

        self.assertEqual(expected, result[0])
        self.assertEqual(original_accumulator, result[1])

    def test_first_puzzle(self):
        expected = 5
        result = first_puzzle(filename="sample_instructions.txt")

        self.assertEqual(expected, result)

    def test_second_puzzle(self):
        expected = 8
        result = second_puzzle(filename="sample_instructions.txt")

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
