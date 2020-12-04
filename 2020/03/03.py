def read_file(name: str):
    return open(name, "r").readlines()

def is_tree(character: str):
    return character == "#"


if __name__ == '__main__':

    hill_map = read_file("input.txt")
    x = 0
    y = 0
    delta_x = 3
    delta_y = 1
    hit_count = 0

    while y < len(hill_map)-1:
        y += delta_y
        x += delta_x

        current_line = hill_map[y].strip()
        fixed_x = x % len(current_line) # linked list for the poor using modulo

        character = current_line[fixed_x]

        if is_tree(character=character):
            print("Ouch! {0}, {1})".format(y, fixed_x))
            hit_count += 1

    print("We hit {0} trees".format(hit_count))