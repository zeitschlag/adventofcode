def first_puzzle
  positions = IO.read("input.txt").split(",")
  
  # 1202 program alarm
  puts "applying 1202 program alarm..."
  positions[1] = 12
  positions[2] = 2
  
  puts "begin calculation..."
  
  0.step(positions.count, 4) { |i|
    opcode = Integer(positions[i])
    
    first_input_index = Integer(positions[i+1])
    first_input_value = Integer(positions[first_input_index])
    
    second_input_index = Integer(positions[i+2])
    second_input_value = Integer(positions[second_input_index])
    output_index = Integer(positions[i+3])
    
    if opcode == 99
      break
    elsif opcode == 1
      result = first_input_value + second_input_value
    elsif opcode == 2
      result = first_input_value * second_input_value
    else
      puts "Weird opcode (#{opcode}), aborting..."
    end
    
    positions[output_index] = result
  
  }
  
  puts "calculation ended. value at position 0: #{positions[0]}"
end


