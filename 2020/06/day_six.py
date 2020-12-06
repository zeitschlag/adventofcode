def read_group_answers(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n\n")


def count_all_answers_in_group(group_answer: str):
    # get rid of newlines
    raw_string = group_answer.replace("\n", "")

    # create set and put every char of the string in it
    unique_answers = set(list(raw_string))

    return len(unique_answers)


def count_same_answers_in_group(group_answer: str):
    # get rid of newlines
    list_of_strings = group_answer.split("\n")
    list_of_sets = list()

    for string in list_of_strings:
        list_of_sets.append(set(list(string)))

    # create set and put every char of the string in it
    common_answers = list_of_sets[0].intersection(*list_of_sets[1:])

    return len(common_answers)


def first_puzzle():
    group_answers = read_group_answers(filename="answers.txt")
    all_answers_per_group = list()

    for group_answer in group_answers:
        answer_in_group = count_all_answers_in_group(group_answer=group_answer)
        all_answers_per_group.append(answer_in_group)

    all_answers = sum(all_answers_per_group)
    print("Sum of answers: {0}".format(all_answers))


def second_puzzle():
    group_answers = read_group_answers(filename="answers.txt")
    all_answers_per_group = list()

    for group_answer in group_answers:
        answer_in_group = count_same_answers_in_group(group_answer=group_answer)
        all_answers_per_group.append(answer_in_group)

    all_answers = sum(all_answers_per_group)
    print("Sum of answers: {0}".format(all_answers))


if __name__ == "__main__":
    second_puzzle()