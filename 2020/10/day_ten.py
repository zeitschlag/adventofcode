def read_int_input(filename: str):
    raw_input = open(filename, "r").read()
    raw_str_list = raw_input.split("\n")
    int_list = list()
    for i in raw_str_list:
        int_list.append(int(i))

    return int_list


def delta(first, second):
    return max([first, second]) - min([first, second])


def highest_joltage_in_list(joltage_list: list):
    return max(joltage_list)


def get_number_of_joltage_differences(joltage_list: list):

    start_voltage = [0]
    sorted_joltage_list = start_voltage + sorted(joltage_list)
    deltas = {"1": 0, "3": 0}

    for i in range(0, len(sorted_joltage_list)-1):
        a = sorted_joltage_list[i]
        b = sorted_joltage_list[i+1]

        needed_adapter = delta(a, b)
        if needed_adapter == 1:
            deltas["1"] += 1
        elif needed_adapter == 3:
            deltas["3"] += 1

    # another one three for the built-in adapter
    deltas["3"] += 1

    return deltas


def count_distinct_adapter_paths(joltage_list):
    pass


def first_part(filename: str):
    joltage_list = read_int_input(filename=filename)
    deltas = get_number_of_joltage_differences(joltage_list=joltage_list)
    result = deltas["1"] * deltas["3"]

    print("The answer should be {0}".format(result))


if __name__ == "__main__":
    first_part(filename="input.txt")