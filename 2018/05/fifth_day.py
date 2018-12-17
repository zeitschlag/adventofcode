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
        # search for lowercaseUPPERCASE

        result = re.search(pattern=pattern, string=content_of_file)

        if result:
            for group in result.groups():
                content_of_file = content_of_file.replace(group, "")
        else:
            unpolarity_found = False

    print("Length of the polymer is %s" % (len(content_of_file)))


if __name__ == "__main__":
    first_puzzle("input.txt")