import unittest
from day_five import calculate_seat_id, get_seat_row, get_seat_column

class MyTestCase(unittest.TestCase):
    def test_seat_id(self):
        row = 44
        column = 5
        expected = 357
        result = calculate_seat_id(row=row, column=column)

        self.assertEqual(expected, result)

    def test_get_row(self):
        seat_string = "FBFBBFFRLR"
        expected = 44
        result = get_seat_row(seat_string=seat_string)

        self.assertEqual(expected, result)

    def test_get_column(self):
        seat_string = "FBFBBFFRLR"
        expected = 5
        result = get_seat_column(seat_string=seat_string)

        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
