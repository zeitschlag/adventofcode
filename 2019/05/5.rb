POSITIONMODE = "0"
IMMEDIATEMODE = "1"

def get_first_parameter_value(command, intcode, index)
  first_input_index = Integer(intcode[index+1])
  first_param_index_mode = command[-3]

  if first_param_index_mode == IMMEDIATEMODE
    first_input_index
  else
    Integer(intcode[first_input_index])
  end
end

def get_second_parameter_value(command, intcode, index)
  second_input_index = Integer(intcode[index+2])
  second_param_index_mode = command[-4]
  
  if second_param_index_mode == IMMEDIATEMODE
    second_input_index
  else
    Integer(intcode[second_input_index])
  end
end

def get_third_parameter_value(command, intcode, index)
  Integer(intcode[index+3])
end

def run_intcode(input)
  
  i = 0 
  loop do
  
    if i == input.length
      break
    end
    
    command = input[i]
    opcode = get_opcode_for_command(command.to_s)
       
    if opcode == :halt
      
      puts "End Program"
      break
      
    elsif opcode == :add
        
      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)   
      output_index = get_third_parameter_value(command, input, i)
      
      result = first_input_value + second_input_value
      input[output_index] = result.to_s
      
    elsif opcode == :multiply

      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)
      output_index = get_third_parameter_value(command, input, i)

      result = first_input_value * second_input_value
      input[output_index] = result.to_s

    elsif opcode == :read

      first_input_value = Integer(input[i+1])
      input[first_input_value] = 5 # first input value, this is a dirty hack
      
    elsif opcode == :write
    
      first_input_index = Integer(input[i+1])
      puts input[first_input_index]

    elsif opcode == :jump_if_true
      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)

      if first_input_value != 0
        i = Integer(second_input_value)
        next
      end

    elsif opcode == :jump_if_false
      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)

      if first_input_value == 0
        i = Integer(second_input_value)
        next
      end

    elsif opcode == :less_than
      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)
      output_index = Integer(input[i+3])
      
      if first_input_value < second_input_value
        input[output_index] = "1"
      else
        input[output_index] = "0"
      end

    elsif opcode == :equals
      first_input_value = get_first_parameter_value(command, input, i)
      second_input_value = get_second_parameter_value(command, input, i)
      output_index = Integer(input[i+3])
      
      parameters_equal = first_input_value == second_input_value
      if parameters_equal
      	input[output_index] = "1"
      else
        input[output_index] = "0"
      end
    else
      raise "Weird opcode (#{opcode} at #{i}), command: #{command}, aborting..."
    end
    
    number_of_parameters = number_of_parameters_for_opcode(opcode)
    
    i += number_of_parameters
    i += 1 # next command
  end
end

def get_opcode_for_command(command)
  if /1$/ =~ command
    :add
  elsif /2$/ =~ command
    :multiply
  elsif /3$/ =~ command
    :read
  elsif /4$/ =~ command
    :write
  elsif /5$/ =~ command
    :jump_if_true
  elsif /6$/ =~ command
    :jump_if_false
  elsif /7$/ =~ command
    :less_than
  elsif /8$/ =~ command
    :equals
  elsif /^99$/ =~ command
    :halt
  end
end

def number_of_parameters_for_opcode(opcode)
  if opcode == :halt
    0
  elsif opcode == :add || opcode == :multiply || opcode == :less_than || opcode == :equals
    3
  elsif opcode == :jump_if_false || opcode == :jump_if_true
    2
  elsif opcode == :read || opcode == :write
    1
  end
end

def first_puzzle 
  intcode = IO.read("input.txt").split(",")
  run_intcode(intcode)
end

first_puzzle