def read_boarding_passes(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n")


def calculate_seat_id(row: int, column: int):
    return row * 8 + column


def get_seat_row(seat_string: str):
    row_string = seat_string[:7]
    binary_string = row_string.replace("B", "1")
    binary_string = binary_string.replace("F", "0")

    return int(binary_string, 2)


def get_seat_column(seat_string: str):
    column_string = seat_string[7:]
    binary_string = column_string.replace("R", "1")
    binary_string = binary_string.replace("L", "0")

    return int(binary_string, 2)


if __name__ == "__main__":
    boarding_passes = read_boarding_passes(filename="boarding_passes.txt")
    seat_ids = list()
    for boarding_pass in boarding_passes:
        row = get_seat_row(boarding_pass)
        column = get_seat_column(boarding_pass)

        seat_id = calculate_seat_id(row=row, column=column)
        seat_ids.append(seat_id)

    # find missing seat. we know: there are 128 rows and 8 seats per row
    # let's brute-force (again)
    for row in range(0, 127):
        for column in range(0, 7):
            seat_id = calculate_seat_id(row=row, column=column)
            if seat_id in seat_ids:
                pass
            else:

                seat_id_plus_one_exists = (seat_id + 1) in seat_ids
                seat_id_minus_one_exists = (seat_id - 1) in seat_ids

                if seat_id_plus_one_exists & seat_id_minus_one_exists:
                    print("Please proceed to ({0}, {1}), Seat-ID: {2}".format(row, column, seat_id))