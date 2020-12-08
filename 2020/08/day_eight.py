OPERATION_ACC = "acc"
OPERATION_JMP = "jmp"
OPERATION_NOP = "nop"

def read_instructions(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n")


def get_operation(instruction: str):
    # split instruction
    # return [0]
    values = instruction.split(" ")
    return str(values[0])


def get_argument(instruction: str):
    values = instruction.split(" ")
    return int(values[1])


def run(operation: str, argument: int, accumulator: int):
    # returns next index relative
    # changes the accumulator
    if operation == OPERATION_NOP:
        # do nothing
        return tuple([1, accumulator])
    elif operation == OPERATION_ACC:
        new_accumulator = accumulator+argument
        return tuple([1, new_accumulator])
    elif operation== OPERATION_JMP:
        return tuple([argument, accumulator])

def first_puzzle(filename: str):

    instructions = read_instructions(filename=filename)
    visited_lines = list()
    accumulator = 0

    # loop doesn't work yet like this
    i = 0
    while i < len(instructions):
        instruction = instructions[i]

        operation = get_operation(instruction=instruction)
        argument = get_argument(instruction=instruction)

        if i in visited_lines:
            return accumulator

        visited_lines.append(i)

        result = run(operation=operation, argument=argument, accumulator=accumulator)
        i += result[0]
        accumulator = result[1]

def second_puzzle(filename: str):
    instructions = read_instructions(filename=filename)
    done = False
    switched_lines = list()

    while not done:
        index = 0
        visited_lines = list()
        accumulator = 0

        while index < len(instructions):

            if index in visited_lines:
                print("infinite loop")
                break

            visited_lines.append(index)

            instruction = instructions[index]

            operation = get_operation(instruction=instruction)
            argument = get_argument(instruction=instruction)

            result = run(operation=operation, argument=argument, accumulator=accumulator)

            index += result[0]
            accumulator = result[1]

        done = False
    print("acc: {0}".format(accumulator))
    return accumulator


if __name__ == "__main__":
    accumulator_value = second_puzzle(filename="instructions.txt")
    print("Last accumulator-value was {0}".format(accumulator_value))