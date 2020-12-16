# Action N means to move north by the given value.
MOVE_NORTH = "N"
# Action S means to move south by the given value.
MOVE_SOUTH = "S"
# Action E means to move east by the given value.
MOVE_EAST = "E"
# Action W means to move west by the given value.
MOVE_WEST = "W"
# Action L means to turn left the given number of degrees.
TURN_LEFT = "L"  # aka counter clock wise
# Action R means to turn right the given number of degrees.
TURN_RIGHT = "R"  # aka clock wise
# Action F means to move forward by the given value in the direction the ship is currently facing.
MOVE_FORWARD = "F"


def read_input(filename):
  with open(filename, "r") as file:
    raw_lines = file.readlines()
    lines = list()
    for line in raw_lines:
      lines.append(line.strip())
    return lines


def manhattan_distance(a, b):
  return abs(a) + abs(b)


def run(instructions: list):

  current_point = {"x": 0, "y": 0}
  facing_angle = 0

  for instruction in instructions:

    action = instruction[:1]
    value = int(instruction[1:])

    if action == MOVE_NORTH:
      current_point["y"] += value
    elif action == MOVE_SOUTH:
      current_point["y"] -= value
    elif action == MOVE_EAST:
      current_point["x"] += value
    elif action == MOVE_WEST:
      current_point["x"] -= value
    elif action == TURN_LEFT:
      facing_angle += value
    elif action == TURN_RIGHT:
      facing_angle -= value
    elif action == MOVE_FORWARD:
      if facing_angle % 360 == 0:
        current_point["x"] += value
      elif facing_angle % 360 == 90:
        current_point["y"] += value
      elif facing_angle % 360 == 180:
        current_point["x"] -= value
      elif facing_angle % 360 == 270:
        current_point["y"] -= value
      else:
        raise RuntimeError("Invalid direction: {0}".format(facing_angle))
    else:
      raise RuntimeError("Invalid action: {0}".format(action))

  return current_point


def run_waypoint(instructions: list):

  current_point = {"x": 0, "y": 0}
  relative_waypoint = {"x": 10, "y": 1}

  for instruction in instructions:

    action = instruction[:1]
    value = int(instruction[1:])

    if action == MOVE_NORTH:
      relative_waypoint["y"] += value
    elif action == MOVE_SOUTH:
      relative_waypoint["y"] -= value
    elif action == MOVE_EAST:
      relative_waypoint["x"] += value
    elif action == MOVE_WEST:
      relative_waypoint["x"] -= value
    elif action == TURN_LEFT or action == TURN_RIGHT:
      # change relative_waypoint
      rotation_angle = value % 360
      old_x = relative_waypoint["x"]
      old_y = relative_waypoint["y"]
      if (action == TURN_RIGHT and rotation_angle == 270) or (
          action == TURN_LEFT and rotation_angle == 90):
        relative_waypoint["x"] = -old_y
        relative_waypoint["y"] = old_x
      elif rotation_angle == 180:
        relative_waypoint["x"] = -old_x
        relative_waypoint["y"] = -old_y
      elif (action == TURN_LEFT and rotation_angle == 270) or (
          action == TURN_RIGHT and rotation_angle == 90):
        relative_waypoint["x"] = old_y
        relative_waypoint["y"] = -old_x
    elif action == MOVE_FORWARD:
      # get the distance between between waypoint and ship
      # move ship value times into X and Y
      delta_x = value * relative_waypoint["x"]
      current_point["x"] += delta_x

      delta_y = value * relative_waypoint["y"]
      current_point["y"] += delta_y

    else:
      raise RuntimeError("Invalid action: {0}".format(action))

  return current_point


def first_part(filename):
  # The Great Plan for Part 1 of Day 12
  # [x] Read Input 
  instructions = read_input(filename=filename)
  # [x] Run Instructions (aka get endpoint)
  endpoint = run(instructions)
  # [x] Calculate Manhattan Distance from Endpoint to Origin (0,0)
  result = manhattan_distance(endpoint["x"], endpoint["y"])
  # 4. Succeed!
  print("Your current position is ({0}, {1}), the Manhattan Distance is {2}".
        format(endpoint["x"], endpoint["y"], result))


def second_part(filename):
  # modify run
  # The Great Plan for Part 1 of Day 12
  # [x] Read Input 
  instructions = read_input(filename=filename)
  # [x] Run Waypoint Instructions (aka get endpoint)
  endpoint = run_waypoint(instructions)
  # [x] Calculate Manhattan Distance from Endpoint to Origin (0,0)
  result = manhattan_distance(endpoint["x"], endpoint["y"])
  # 4. Succeed!
  print("Your current position is ({0}, {1}), the Manhattan Distance is {2}".
        format(endpoint["x"], endpoint["y"], result))


if __name__ == "__main__":
  second_part(filename="input.txt")

