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
  
  def eql?(other_object)
    return @x == other_object.x && @y == other_object.y
  end
  
  def hash
    return [@x, @y].hash
  end

end

class Wire_Path
  
  attr_reader :coordinates
  
  def initialize(starting_point, instructions)
    @starting_point = starting_point
    @coordinates = get_coordinates_from_instructions(instructions)
    @sorted_coordinates = get_coordinates_list_from_instructions(instructions)
  end

  def get_coordinates_from_instructions(instructions)
    current_point = @starting_point
    instruction_list = instructions.split(",")
    all_points = Set[]
      
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
  
  def get_coordinates_list_from_instructions(instructions)
    current_point = @starting_point
    instruction_list = instructions.split(",")
    all_points = Array[]
      
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
        all_points.append(new_point)
        current_point = new_point
      end
    end
  
    return all_points
  end
  
  def get_coordinates_until_intersection(intersection)
    coordinates = []
    
    for coordinate in @sorted_coordinates do
      if coordinate.x == intersection.x && coordinate.y == intersection.y
        coordinates.append(coordinate)
        break
      else
        coordinates.append(coordinate)
      end
    end

    return coordinates
  end
  
end

def first_puzzle
  central_port = Coordinate.new(x=0, y=0)
  
  wire_instructions = IO.read("input.txt").split("\n")
  wire_paths = []
  
  for wire_instruction in wire_instructions do
    wire_path = Wire_Path.new(central_port, wire_instruction)
    wire_paths.append(wire_path)
  end
  
  intersections = Set[]
  
  for i in wire_paths do
    for j in wire_paths do
      
      if i == j
        next
      end
        
      intersection = (i.coordinates & j.coordinates)
      intersection.each do |i|
        intersections.add(i)
      end
    end
  end

  distance_of_closest_intersection = intersections.min { |a, b|
    a.calculate_manhattan_distance(central_port) <=> b.calculate_manhattan_distance(central_port)
  }
  
  puts "distance of closest intersection is #{distance_of_closest_intersection.calculate_manhattan_distance(central_port)}"
end

first_puzzle