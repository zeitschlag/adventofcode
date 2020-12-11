EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


def read_seat_map(filename):
    seat_map = list()

    lines = open(filename, "r").read().split("\n")
    for line in lines:
        row = list(line)
        seat_map.append(row)
    return seat_map


def stabilize_seat_map(seat_map):
    stabilized = False
    old_seat_map = seat_map

    while not stabilized:
         new_seat_map = generate_new_seat_map(old_seat_map=old_seat_map)
         stabilized = (new_seat_map == old_seat_map)
         old_seat_map = new_seat_map

    return old_seat_map


def generate_new_seat_map(old_seat_map):
    new_seat_map = list()

    for row_index in range(len(old_seat_map)):
        old_row = old_seat_map[row_index]
        new_row = list()
        for column_index in range(len(old_row)):
            old_seat = old_row[column_index]

            number_adjacent_occupied_seats = get_number_adjacent_occupied_seats(row=row_index, column=column_index, seat_map=old_seat_map)
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if (old_seat == EMPTY_SEAT) & (number_adjacent_occupied_seats == 0):
                new_seat = OCCUPIED_SEAT
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elif (old_seat == OCCUPIED_SEAT) & (number_adjacent_occupied_seats >= 4):
                new_seat = EMPTY_SEAT
            else:
                # Otherwise, the seat's state does not change.
                new_seat = old_seat

            new_row.append(new_seat)

        new_seat_map.append(new_row)
    return new_seat_map


def get_number_adjacent_occupied_seats(row, column, seat_map):
    adjacent_seats = []

    # [i - 1, j - 1], [i - 1, j], [i - 1, j + 1]
    if row > 0:
        if column > 0:
            try:
                upper_left_seat = seat_map[row-1][column-1]
                adjacent_seats.append(upper_left_seat)
            except IndexError:
                pass

        try:
            upper_seat = seat_map[row - 1][column]
            adjacent_seats.append(upper_seat)
        except IndexError:
            pass

        if column < len(seat_map[row]):
            try:
                upper_right_seat = seat_map[row-1][column+1]
                adjacent_seats.append(upper_right_seat)
            except IndexError:
                pass

    # [i, j - 1], [_, _], [i, j + 1]
    if column > 0:
        try:
            left_seat = seat_map[row][column - 1]
            adjacent_seats.append(left_seat)
        except IndexError:
            pass

    if column < len(seat_map[row]):
        try:
            right_seat = seat_map[row][column+1]
            adjacent_seats.append(right_seat)
        except IndexError:
            pass

    # [i + 1], [i + 1, j], [i + 1, j + 1]
    if row < len(seat_map):
        if column > 0:
            try:
                lower_left_seat = seat_map[row+1][column-1]
                adjacent_seats.append(lower_left_seat)
            except IndexError:
                pass

        try:
            lower_seat = seat_map[row+1][column]
            adjacent_seats.append(lower_seat)
        except IndexError:
            pass

        if column < len(seat_map[row]):
            try:
                lower_right_seat = seat_map[row+1][column+1]
                adjacent_seats.append(lower_right_seat)
            except IndexError:
                pass

    return count_occupied_seats(adjacent_seats)


def count_occupied_seats(seat_map):
    all_seats = ""
    for seat_row in seat_map:
        all_seats += "".join(seat_row)

    return all_seats.count(OCCUPIED_SEAT)


def first_part(filename):
    seat_map = read_seat_map(filename=filename)
    stabilized_seatmap = stabilize_seat_map(seat_map=seat_map)
    occupied_seats = count_occupied_seats(seat_map=stabilized_seatmap)
    print("There are {0} occupied seats in the stabilized seat map".format(occupied_seats))



if __name__ == "__main__":
    first_part(filename="input.txt")