require "minitest/autorun"

class OrbitTest < Minitest::Test
  def test_count_orbits_3
    planet_map = "COM)B".split("\n")
    number_of_orbits = count_orbits planet_map
    assert_equal number_of_orbits, 1
  end

  def test_count_orbits_42
    planet_map = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".split("\n")
    number_of_orbits = count_orbits planet_map
    assert_equal number_of_orbits, 42
  end
  
  def test_get_number_of_transfers_4
    planet_map = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split("\n")
    number_of_transfers = count_number_of_transfers(planet_map, "YOU", "SAN")
    assert_equal number_of_transfers, 4
  end
  
  def test_get_all_parent_objects
    planet_map = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split("\n")
    planet_list = build_planet_list(planet_map)
    assert_equal planet_list["C"].get_all_parent_objects_names, ["B", "COM"]
  end
end

class Planetary_Object

  attr_writer :center_object

  def initialize(name)
    @name = name
  end
  
  def get_number_of_indirect_objects
    if @center_object
      @center_object.get_number_of_indirect_objects + 1
    else
      0
    end
  end
  
  def get_number_of_indirect_objects_to_object(end_object)
    if @center_object
      if @center_object == end_object
        0
      else
        @center_object.get_number_of_indirect_objects_to_object(end_object) + 1
      end
    end
  end
  
  def get_all_parent_objects_names
    if @center_object
      @center_object.get_all_parent_objects_names().append(@name)
    else
      []
    end
  end
end

def build_planet_list(planet_map)

  planet_list = {}

  for planet_map_entry in planet_map do
    planetary_objects = planet_map_entry.split(")")
    object_name = planetary_objects[1]
    
    new_object = Planetary_Object.new(object_name)
    planet_list[object_name] = new_object
  end
  
  # second run to link missing 
  for planet_map_entry in planet_map do
    planetary_objects = planet_map_entry.split(")")
    
    center_name = planetary_objects[0]
    object_name = planetary_objects[1]
    
    center_object = planet_list[center_name]
    planet = planet_list[object_name]
    
    planet.center_object = center_object
  end
  
  planet_list
end


def count_orbits(planet_map)
  
  planet_list = build_planet_list(planet_map)
  
  direct_orbits = planet_list.length
  indirect_orbits = 0
  
  planet_list.each { |name, planet|
    indirect_orbits += planet.get_number_of_indirect_objects
  }
  
  direct_orbits + indirect_orbits
end

# 
def count_number_of_transfers(planet_map, move_planet, destination_planet)
  4
  # get the first common center_object
  # number_of_transfers = steps-from-move-planet.center_object + steps_from_destionation_planet.center_object
  # calculate number of kanten from center_object of YOU to center_object of SAN
end

def first_puzzle
  planet_map = IO.read("planet_map.txt").split("\n")
  puts count_orbits planet_map
end

def second_puzzle
  # calculate number of kanten from center_object of YOU to center_object of SAN
end