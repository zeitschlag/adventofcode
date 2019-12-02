def run_intcode(input)
  
  puts "begin calculation..."
  
  0.step(input.count, 4) { |i|
    opcode = Integer(input[i])
    
    first_input_index = Integer(input[i+1])
    first_input_value = Integer(input[first_input_index])
    
    second_input_index = Integer(input[i+2])
    second_input_value = Integer(input[second_input_index])
    output_index = Integer(input[i+3])
    
    if opcode == 99
      break
    elsif opcode == 1
      result = first_input_value + second_input_value
    elsif opcode == 2
      result = first_input_value * second_input_value
    else
      puts "Weird opcode (#{opcode} at #{i}), aborting..."
    end
    
    input[output_index] = result
  
  }

  return Integer(input[0])
  
end

def first_puzzle 
  positions = IO.read("input.txt").split(",")
  puts "applying 1202 program alarm..."
  positions[1] = 12
  positions[2] = 2
  result = run_intcode(positions) 
  
  puts "calculation ended. value at position 0: #{result}"
end

