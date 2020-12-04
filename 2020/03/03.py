def read_file(name: str):
    return open(name, "r").readlines()


def is_tree(character: str):
    return character == "#"


if __name__ == '__main__':

    from collections import namedtuple

    Slope = namedtuple("Slope", "x, y")
    slopes = [
        Slope(x=1, y=1),
        Slope(x=3, y=1),
        Slope(x=5, y=1),
        Slope(x=7, y=1),
        Slope(x=1, y=2),
    ]

    answer = 1

    for slope in slopes:
        hit_count = 0

        hill_map = read_file("input.txt")
        x = 0
        y = 0

        while y < len(hill_map)-1:
            y += slope.y
            x += slope.x

            current_line = hill_map[y].strip()
            fixed_x = x % len(current_line) # linked list for the poor using modulo
            character = current_line[fixed_x]

            if is_tree(character=character):
                hit_count += 1

        print("We hit {0} trees".format(hit_count))
        answer *= hit_count

    print("Answer is {0}".format(answer))