import unittest
from day_seven import *


class DaySevenPuzzleOneTests(unittest.TestCase):
    def test_bright_white_contains_shiny_gold_bag(self):
        # rule = "bright white bags contain 1 shiny gold bag"
        rules = {"bright white": ["shiny gold"]}
        bag_color = "bright white"
        expected = True
        result = bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)

    def test_light_red_contains_shiny_gold_bag(self):
        # rule = "bright white bags contain 1 shiny gold bag"
        rules = {"bright white": ["shiny gold"], "light red": ["bright white", "muted yellow"]}
        bag_color = "light red"
        expected = True
        result = bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)

    def test_contains_no_bag(self):
        # dotted black bags contain no other bags.
        rules = {"dotted black": []}
        bag_color = "dotted black"
        expected = False
        result = bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)

    def test_gold_shiny(self):
        # dotted black bags contain no other bags.
        rules = {"shiny gold": ["dark olive", "vibrant plum"]}
        bag_color = "shiny gold"
        expected = False
        result = bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)

    def test_parse_rule_no_bags(self):
        raw_rule = ["dotted black bags contain no other bags."]
        expected = {"dotted black": []}
        result = parse_rules(list_of_rules=raw_rule)
        self.assertEqual(expected, result)

    def test_parse_rule_dark_olive(self):
        raw_rule = ["dark olive bags contain 3 faded blue bags, 4 dotted black bags."]
        expected = {"dark olive": ["faded blue", "dotted black"]}
        result = parse_rules(list_of_rules=raw_rule)
        self.assertEqual(expected, result)

    def test_first_puzzle(self):
        expected = 4
        result = first_puzzle(filename="sample_input.txt")
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
