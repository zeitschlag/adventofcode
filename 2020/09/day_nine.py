def read_input(filename: str):
    raw_input = open(filename, "r").read()
    raw_str_list = raw_input.split("\n")
    int_list = list()
    for i in raw_str_list:
        int_list.append(int(i))

    return int_list


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


def find_weakness(number: int, code_list: list):

    minimum_slice_length = 2
    maximum_slice_length = len(code_list)-1
    index_of_invalid_number = code_list.index(number)

    # generate all sliced lists
    slices = list()
    for i in range(index_of_invalid_number):
        for j in range(1, index_of_invalid_number):
            new_slice = code_list[i:j+1]
            if len(new_slice)>=minimum_slice_length:
                slices.append(new_slice)

    for slice in slices:
        if sum(slice) == number:
            return slice


def find_first_invalid_number(filename: str, length: int):
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


def second_part(filename: str, length: int):
    xmas_codes = read_input(filename=filename)
    first_invalid_number = find_first_invalid_number(filename=filename, length=length)
    contigious_numbers = find_weakness(number=first_invalid_number, code_list=xmas_codes)

    return sum([min(contigious_numbers), max(contigious_numbers)])

if __name__ == "__main__":

    encryption_weakness = second_part(filename="input.txt", length=25)
    print("Encryption Weakness: {0}".format(encryption_weakness))