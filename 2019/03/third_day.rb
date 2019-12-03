require 'set'

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

class Wire_Path
  
  attr_reader :coordinates
  
  def initialize(starting_point, instructions)
    @starting_point = starting_point
    @coordinates = get_coordinates_from_instructions(instructions)
  end

  def get_coordinates_from_instructions(instructions)
    current_point = @starting_point
    instruction_list = instructions.split(",")
    all_points = Set[current_point]
      
    instruction_list.each do |instruction|
      direction = instruction[0]
      length = Integer(instruction[1..-1])
      
      dx = 0
      dy = 0
                
      if direction == "R"
        dx = 1
      elsif direction == "L"  
        dx = -1
      elsif direction == "U"
        dy = 1
      elsif direction == "D"
        dy = -1
      end
      
      for i in 0...length do
        new_point = Coordinate.new(x=current_point.x+dx, y=current_point.y+dy)
        all_points.add(new_point)
        current_point = new_point
      end
      
    end    
  
    return all_points
  end
end

central_port = Coordinate.new(x=0, y=0)

wire_instructions = IO.read("input.txt").split("\n")


# first idea:
# central port: 0, 0, although it doesn't matter
# read wire-paths, each path is in one line
# calculate all points for all paths
# crossing points are points, that are in both paths
# calculate the manhattan-distance for all crossing points to the central port
# loweset manhattan distance is the answer
