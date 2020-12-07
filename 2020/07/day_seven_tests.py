import unittest
from day_seven import *


class DaySevenPuzzleOneTests(unittest.TestCase):
    def test_bright_white_contains_shiny_gold_bag(self):
        # rule = "bright white bags contain 1 shiny gold bag"
        rules = {"bright white": [{"color": "shiny gold", "amount": 1}]}
        bag_color = "bright white"
        expected = True
        result = bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)

    def test_light_red_contains_shiny_gold_bag(self):
        # rule = "bright white bags contain 1 shiny gold bag"
        # rule = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        rules = {"bright white": [{"color": "shiny gold", "amount": 1}],
                 "light red": [{"color": "bright white", "amount": 1}, {"color": "muted yellow", "amount": 2}]}

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
        # shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        rules = {"shiny gold": [{"color": "dark olive", "amount": 1}, {"color": "vibrant plum", "amount": 2}]}
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
        expected = {"dark olive": [{"color": "faded blue", "amount": 3}, {"color": "dotted black", "amount": 4}]}
        result = parse_rules(list_of_rules=raw_rule)
        self.assertEqual(expected, result)

    def test_amount_of_subbags(self):
        rules = {
            "shiny gold": [],
            "bright white": [{"color": "shiny gold", "amount": 1}],
            "light red": [{"color": "bright white", "amount": 1},
                          {"color": "muted yellow", "amount": 2}]}

        bag_color = "bright white"
        expected = 1
        result = sub_amounts(bag_color=bag_color, rules=rules)
        self.assertEqual(expected, result)


    def test_first_puzzle(self):
        expected = 4
        result = first_puzzle(filename="sample_input.txt")
        self.assertEqual(expected, result)

    def test_second_puzzle(self):
        expected = 32
        result = second_puzzle(filename="sample_input.txt")
        self.assertEqual(expected, result)

    def test_vibrant_plum(self):
        raw_rules = read_rules(filename="sample_input.txt")
        rules = parse_rules(list_of_rules=raw_rules)

        expected = 11
        result = sub_amounts(bag_color="vibrant plum", rules=rules)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
