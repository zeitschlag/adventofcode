import unittest
from day_13 import *


class DayThirteenUnitTests(unittest.TestCase):
  def test_read_input(self):
    expected = ["939", ["7", "13", "x", "x", "59", "x", "31", "19"]]
    result = read_input(filename="sample_input.txt")
    self.assertListEqual(result, expected)

  def test_get_timestamp(self):
    notes = ["939", ["7", "13", "x", "x", "59", "x", "31", "19"]]
    expected = 939
    result = get_timestamp(notes)

    self.assertEqual(result, expected)

  def test_get_valid_buses(self):
    notes = ["939", ["7", "13", "x", "x", "59", "x", "31", "19"]]
    expected = [7, 13, 59, 31, 19]
    result = get_valid_buses(notes)

    self.assertListEqual(result, expected)

  def test_get_earliest_bus(self):
    bus_list = [7, 13, 59, 31, 19]
    timestamp = 939
    expected = {"timestamp": 944, "id": 59}
    result = get_earliest_bus(timestamp, bus_list)

    self.assertDictEqual(result, expected)

  def test_first_part(self):
    expected = 295
    result = first_part(filename="sample_input.txt")

    self.assertEqual(result, expected)


if __name__ == "__main__":
  unittest.main()

