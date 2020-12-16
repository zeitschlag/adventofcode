import unittest
from day_12 import *


class DayTwelveTests(unittest.TestCase):
  def test_read_input(self):
    expected = ["F10", "N3", "F7", "R90", "F11"]
    result = read_input(filename="sample_input.txt")
    self.assertListEqual(result, expected)
  
  def test_manhattan_distance_8_17(self):
    expected = 25
    result = manhattan_distance(8, 17)
    self.assertEqual(result, expected)
    
  def test_manhattan_distance_8_minus_17(self):
    expected = 25
    result = manhattan_distance(8, -17)
    self.assertEqual(result, expected)
    
  def test_manhattan_distance_minus_8_17(self):
    expected = 25
    result = manhattan_distance(-8, 17)
    self.assertEqual(result, expected)
    
  def test_manhattan_distance_minus_8_minus_17(self):
    expected = 25
    result = manhattan_distance(-8, -17)
    self.assertEqual(result, expected)  
  
  def test_run_instructions(self):
    instructions = ["F10", "N3", "F7", "R90", "F11"]
    expected_endpoint = {"x": 17, "y": -8}
    calculated_endpoint = run(instructions=instructions)
    
    self.assertDictEqual(calculated_endpoint, expected_endpoint)
    
  def test_run_waypoint_instructions(self):
    instructions = ["F10", "N3", "F7", "R90", "F11"]
    expected_endpoint = {"x": 214, "y": -72}
    calculated_endpoint = run_waypoint(instructions=instructions)
    
    self.assertDictEqual(calculated_endpoint, expected_endpoint)
  
if __name__ == "__main__":
  unittest.main()
