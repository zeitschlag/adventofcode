def read_rules(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n")


def parse_rules(list_of_rules: list):
    # rule = {"color": ["color", color"]}
    rules = dict()

    for raw_rule in list_of_rules:
        key_rules = raw_rule.split(" bags contain ")
        key = key_rules[0]
        bag_colors: str = key_rules[1]

        if bag_colors == "no other bags.":
            rules[key] = []
        else:
            # 2 shiny gold bags, 9 faded blue bags.
            bag_color_list = bag_colors.replace(".", "").split(",")
            values = list()
            for bag_color in bag_color_list:
                bag_color_without_bag = bag_color.replace(" bags", "").replace(" bag", "").strip()
                bag_color_without_number = " ".join(bag_color_without_bag.split(" ")[1:])
                values.append(bag_color_without_number)

            rules[key] = values

    return rules


def bag_contains_shiny_gold_bag(bag_color: str, rules: dict):
    shiny_gold = "shiny gold"
    if bag_color == shiny_gold:
        return False
    elif shiny_gold in rules[bag_color]:
        return True
    elif rules[bag_color] == []:
        return False
    else:
        # Recursive
        sub_bag_rules_list = list(rules[bag_color])
        for sub_bag_rule in sub_bag_rules_list:
            if bag_contains_shiny_gold_bag(sub_bag_rule, rules=rules):
                return True

        return False


def first_puzzle(filename: str):
    raw_rules = read_rules(filename=filename)
    rules = parse_rules(list_of_rules=raw_rules)

    bags_containing_gold = 0
    for bag_color in rules:
        if bag_contains_shiny_gold_bag(bag_color=bag_color, rules=rules):
            bags_containing_gold += 1

    return bags_containing_gold


if __name__ == "__main__":
    number_of_rules_containing_gold = first_puzzle(filename="input.txt")
    print(number_of_rules_containing_gold)