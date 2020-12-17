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

    new_bus = int(bus)
    valid_buses.append(new_bus)

  return valid_buses


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


def first_part(filename):

  notes = read_input(filename=filename)
  earliest_possible_timestamp = get_timestamp(notes)
  bus_list = get_valid_buses(notes)

  first_bus = get_earliest_bus(earliest_possible_timestamp, bus_list)

  waiting_time = first_bus["timestamp"] - earliest_possible_timestamp

  result = waiting_time * first_bus["id"]
  return result


if __name__ == "__main__":
  print("The solution for the first part is {0}".format(
    first_part(filename="input.txt")))

