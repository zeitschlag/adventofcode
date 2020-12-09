def read_input(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n")


def preamble(code: list, offset: int, length):
    return code[offset:offset+length]


def is_number_valid(number: int, code_list: list):
    # number is valid if there are exactly two numbers in code_list
    # -> Create a new list of all first+second, with first!=second
    # where first_number + second_number = number

    sums = list()
    for i in code_list:
        for j in code_list:
            if i != j:
                sums.append(int(i)+int(j))

    return int(number) in sums


def first_part(filename: str, length: int):
    # iterate over all codes, first preamble first 25 charts.
    # check each number afterwards:
    # if valid:
        # change preamble, remove the first number, add the current number
        # aka: increase the offset and create check the list
    # else:
        # we found the invalid number
    xmas_codes = read_input(filename=filename)

    intial_preamble = preamble(code=xmas_codes, offset=0, length=length)
    code_list = intial_preamble
    initial_offset = len(code_list)
    offset_counter = 0

    for i in range(initial_offset, len(xmas_codes)-1):
        number = xmas_codes[i]
        if is_number_valid(number=int(number), code_list=code_list):
            offset_counter += 1
            code_list = preamble(code=xmas_codes, offset=offset_counter, length=length)
            continue
        else:
            return int(number)


if __name__ == "__main__":
    first_invalid_number = first_part(filename="input.txt", length=25)
    print("First invalid number: {0}".format(first_invalid_number))