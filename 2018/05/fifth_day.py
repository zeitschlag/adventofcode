import re
import string


def first_puzzle(input_file_path):

    polymer = open(input_file_path, "r").read()
    regexlist = list()
    reaction_pattern = get_full_reaction_pattern()
    polymer = fully_react(polymer=polymer, pattern=reaction_pattern)
    print("Length of the polymer is %s" % (len(polymer)))


def second_puzzle(input_file_path):
    polymer = open(input_file_path, "r").read()
    shortest_polymer = len(polymer)
    shortest_polymer_pattern = None
    reaction_pattern = get_full_reaction_pattern()

    for lowercase in string.ascii_lowercase:
        polymer = open(input_file_path, "r").read()
        pattern = "(%s|%s)" % (lowercase, lowercase.upper())

        # remove all letters of one kind
        polymer = fully_react(polymer=polymer, pattern=pattern)
        # do the usual reaction-thing
        polymer = fully_react(polymer=polymer, pattern=reaction_pattern)

        if len(polymer) < shortest_polymer:
            shortest_polymer = len(polymer)
            shortest_polymer_pattern = pattern

    print("Length of shortest polymer: %s (Pattern: %s)" % (shortest_polymer, shortest_polymer_pattern))


def fully_react(polymer, pattern):
    unpolarity_found = True
    while unpolarity_found:
        result = re.search(pattern=pattern, string=polymer)

        if result:
            for group in result.groups():
                polymer = polymer.replace(group, "")
        else:
            unpolarity_found = False
    return polymer


def get_full_reaction_pattern():
    reaction_regex_list = list()
    for i in string.ascii_lowercase:
        for j in string.ascii_uppercase:
            if i.lower() == j.lower():
                reaction_regex_list.append("%s%s" % (i, j))
                reaction_regex_list.append("%s%s" % (j, i))

    reaction_pattern = "|".join(reaction_regex_list)
    reaction_pattern = "(" + reaction_pattern + ")"

    return reaction_pattern


if __name__ == "__main__":
    first_puzzle("input.txt")
    second_puzzle("input.txt")