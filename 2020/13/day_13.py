def read_input(filename):
  with open(filename, "r") as file:
    raw_lines = file.readlines()

    notes = list()
    notes.append(raw_lines[0].strip())
    buses = raw_lines[1].split(",")

    notes.append(buses)
    return notes


def get_timestamp(notes):
  return int(notes[0])


def get_valid_buses(notes):
  bus_list = notes[1]
  valid_buses = list()

  for bus in bus_list:

    if bus == "x":
      continue

    new_bus = int(bus.strip())
    valid_buses.append(new_bus)

  return valid_buses


def get_buses(notes):
  bus_list = notes[1]
  return bus_list


def get_earliest_bus(earliest_timestamp, bus_list):

  minimum = 0
  bus_id = None
  bus_timestamp = None
  current_waiting_time = earliest_timestamp

  for bus in bus_list:
    earlierst_bus_timestamp = (int(earliest_timestamp / bus) + 1) * bus
    waiting_time = earlierst_bus_timestamp - earliest_timestamp

    if waiting_time < current_waiting_time:
      current_waiting_time = waiting_time
      bus_id = bus
      bus_timestamp = earlierst_bus_timestamp

  return {"id": bus_id, "timestamp": bus_timestamp}


def find_earliest_timestamp(bus_list: list, valid_buses, starting_point):

  found_number = False
  delta = valid_buses[0]
  candidate = starting_point

  while not found_number:

    # for all in valid_buses
    for_all = True
    for bus in valid_buses[1:]:
      index = bus_list.index(str(bus))
      is_valid = (candidate % bus) == (bus - index)
      if not is_valid:
        for_all = False
        break

    found_number = for_all
    if not found_number:
      candidate += delta
  
  return candidate


def first_part(filename):

  notes = read_input(filename=filename)
  earliest_possible_timestamp = get_timestamp(notes)
  bus_list = get_valid_buses(notes)

  first_bus = get_earliest_bus(earliest_possible_timestamp, bus_list)

  waiting_time = first_bus["timestamp"] - earliest_possible_timestamp

  result = waiting_time * first_bus["id"]
  return result


def second_part(filename):
  notes = read_input(filename=filename)
  earliest_possible_timestamp = get_timestamp(notes)
  valid_buses = get_valid_buses(notes)
  bus_list = get_buses(notes)
  starting_point = 0 #  100000000000004
  earliest_timestamp = find_earliest_timestamp(
    bus_list=bus_list, valid_buses=valid_buses, starting_point=starting_point)

  return earliest_timestamp


if __name__ == "__main__":
  print("The solution for the first part is {0}".format(
    first_part(filename="input.txt")))
  print("The solution for the second part is {0}".format(
    second_part(filename="input.txt")))

