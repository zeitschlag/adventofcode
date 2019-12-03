class Coordinate

  attr_reader :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def calculate_manhattan_distance(other_point)
    return (@x - other_point.x).abs + (@y - other_point.y).abs
  end

end

class Path
  def initialize(central_port, instructions)
    @central_port = central_port

    @points = get_coordinates_from_instructions(instructions)
  end

  def get_coordinates_from_instructions(instructions)
    return [Coordinate.new(1, 1)]
  end
end

central_port = Coordinate.new(x=0, y=0)

# first idea:
# central port: 0, 0
# read wire-paths, each path is in one line
# calculate all points for all paths
# crossing points are points, that are in both paths
# calculate the manhattan-distance for all crossing points to the central port
# loweset manhattan distance is the answer
