import re
import string


def first_puzzle(input_file_path):

    content_of_file = open(input_file_path, "r").read()
    unpolarity_found = True
    regexlist = list()

    for i in string.ascii_lowercase:
        for j in string.ascii_uppercase:
            if i.lower() == j.lower():
                regexlist.append("%s%s" % (i, j))
                regexlist.append("%s%s" % (j, i))

    pattern = "|".join(regexlist)
    pattern = "(" + pattern + ")"

    while unpolarity_found:
        result = re.search(pattern=pattern, string=content_of_file)

        if result:
            for group in result.groups():
                content_of_file = content_of_file.replace(group, "")
        else:
            unpolarity_found = False

    print("Length of the polymer is %s" % (len(content_of_file)))

def second_puzzle(input_file_path):
    content_of_file = open(input_file_path, "r").read()
    shortest_polymer = len(content_of_file)
    reaction_regex_list = list()

    for i in string.ascii_lowercase:
        for j in string.ascii_uppercase:
            if i.lower() == j.lower():
                reaction_regex_list.append("%s%s" % (i, j))
                reaction_regex_list.append("%s%s" % (j, i))

    reaction_pattern = "|".join(reaction_regex_list)
    reaction_pattern = "(" + reaction_pattern + ")"

    for lowercase in string.ascii_lowercase:
        UPPERCASE = lowercase.upper()

        content_of_file = open(input_file_path, "r").read()
        pattern = "(%s|%s)" % (lowercase, UPPERCASE)

        # remove all letters of one kind
        all_letters_replaced = True
        while all_letters_replaced:
            result = re.search(pattern=pattern, string=content_of_file)
            if result:
                for group in result.groups():
                    content_of_file = content_of_file.replace(group, "")
            else:
                all_letters_replaced = False

        # do the usual reaction-thing
        unpolarity_found = True
        while unpolarity_found:
            result = re.search(pattern=reaction_pattern, string=content_of_file)

            if result:
                for group in result.groups():
                    content_of_file = content_of_file.replace(group, "")
            else:
                unpolarity_found = False

        if len(content_of_file) < shortest_polymer:
            shortest_polymer = len(content_of_file)

    print("Length of shortest polymer: %s" % (shortest_polymer))


if __name__ == "__main__":
    first_puzzle("input.txt")
    second_puzzle("input.txt")