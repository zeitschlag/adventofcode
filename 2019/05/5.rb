def run_intcode(input)

  position_mode = "0"
  immediate_mode = "1"
   
  i = 0 
  loop do
  
  	if i == input.length
  	  break
  	end
  	
  	command = input[i]
    opcode = get_opcode_for_command(command.to_s)

    # check each parameter for being direct input or address
        
    if opcode == :halt
      
      puts "End Program"
      break
      
    elsif opcode == :add
    
      first_input_index = Integer(input[i+1])
      first_param_index_mode = command[-3]
      
      if first_param_index_mode == immediate_mode
        first_input_value = first_input_index
      else
        first_input_value = Integer(input[first_input_index])
      end

      second_input_index = Integer(input[i+2])
      second_param_index_mode = command[-4]
      
      if second_param_index_mode == immediate_mode
        second_input_value = second_input_index
      else
        second_input_value = Integer(input[second_input_index])
      end
      
      output_index = Integer(input[i+3])
      third_param_index_mode = command[-5]
      if third_param_index_mode == immediate_mode
      	output_value = output_index
      else
        output_value = Integer(input[output_index])
      end

      result = first_input_value + second_input_value
      input[output_index] = result
      
    elsif opcode == :multiply

      first_input_index = Integer(input[i+1])
      first_param_index_mode = command[-3]
      
      if first_param_index_mode == immediate_mode
        first_input_value = first_input_index
      else
        first_input_value = Integer(input[first_input_index])
      end

      second_input_index = Integer(input[i+2])
      second_param_index_mode = command[-4]
      
      if second_param_index_mode == immediate_mode
        second_input_value = second_input_index
      else
        second_input_value = Integer(input[second_input_index])
      end
      
      output_index = Integer(input[i+3])
      third_param_index_mode = command[-5]
      if third_param_index_mode == immediate_mode
      	output_value = output_index
      else
        output_value = Integer(input[output_index])
      end

      result = first_input_value * second_input_value
      input[output_index] = result

    elsif opcode == :read

      first_input_index = Integer(input[i+1])
      first_param_index_mode = command[-3]
      
      if first_param_index_mode == immediate_mode
        first_input_value = first_input_index
      else
        first_input_value = Integer(input[first_input_index])
      end

      first_input_value = Integer(input[i+1])
      input[first_input_value] = 1 # first input value, this is a dirty hack
      
    elsif opcode == :write
    
      first_input_index = Integer(input[i+1])
      puts input[first_input_index]
    
    else
      puts "Weird opcode (#{opcode} at #{i}), aborting..."
    end
    
    number_of_parameters = number_of_parameters_for_opcode(opcode)
    
    i += number_of_parameters
    i += 1 # next command
  end
end

def get_opcode_for_command(command)
  if /1$/ =~ command
    return :add
  elsif /2$/ =~ command
    return :multiply
  elsif /3$/ =~ command
    return :read
  elsif /4$/ =~ command
    return :write
  elsif /^99$/ =~ command
    return :halt
  end
end

def number_of_parameters_for_opcode(opcode)
  if opcode == :halt
    return 0
  elsif opcode == :add || opcode == :multiply
    return 3
  elsif opcode == :read || opcode == :write
    return 1
  end
end

def first_puzzle 
  intcode = IO.read("input.txt").split(",")
  result = run_intcode(intcode) 
end

# get opcode: i.to_s[-2, 2]

first_puzzle