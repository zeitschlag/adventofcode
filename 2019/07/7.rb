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

# take intcode, and input to
def run_intcode(intcode, phase_setting, input_value)
  
  i = 0 
  loop do
  
    if i == intcode.length
      break
    end
    
    command = intcode[i]
    opcode = get_opcode_for_command(command.to_s)
       
    if opcode == :halt
      
      puts "End Program"
      break
      
    elsif opcode == :add
        
      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)   
      output_index = get_third_parameter_value(command, intcode, i)
      
      result = first_input_value + second_input_value
      intcode[output_index] = result.to_s
      
    elsif opcode == :multiply

      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)
      output_index = get_third_parameter_value(command, intcode, i)

      result = first_input_value * second_input_value
      intcode[output_index] = result.to_s

    elsif opcode == :read

      first_input_value = Integer(intcode[i+1])
      intcode[first_input_value] = 5 # first input value, this is a dirty hack. Will be modified now.
      
    elsif opcode == :write
    
      first_input_index = Integer(intcode[i+1])
      puts intcode[first_input_index]

    elsif opcode == :jump_if_true
      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)

      if first_input_value != 0
        i = Integer(second_input_value)
        next
      end

    elsif opcode == :jump_if_false
      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)

      if first_input_value == 0
        i = Integer(second_input_value)
        next
      end

    elsif opcode == :less_than
      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)
      output_index = Integer(intcode[i+3])
      
      if first_input_value < second_input_value
        intcode[output_index] = "1"
      else
        intcode[output_index] = "0"
      end

    elsif opcode == :equals
      first_input_value = get_first_parameter_value(command, intcode, i)
      second_input_value = get_second_parameter_value(command, intcode, i)
      output_index = Integer(intcode[i+3])
      
      parameters_equal = first_input_value == second_input_value
      if parameters_equal
        intcode[output_index] = "1"
      else
        intcode[output_index] = "0"
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
  if command.end_with?("1")
    :add
  elsif command.end_with?("2")
    :multiply
  elsif command.end_with?("3")
    :read
  elsif command.end_with?("4")
    :write
  elsif command.end_with?("5")
    :jump_if_true
  elsif command.end_with?("6")
    :jump_if_false
  elsif command.end_with?("7")
    :less_than
  elsif command.end_with?("8")
    :equals
  elsif command.end_with?("99")
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
  intcode = IO.read("AmplifierControllerSoftware.txt").split(",")
  # run intcode in different input orders
  run_intcode(intcode, 0, 0)
end

first_puzzle