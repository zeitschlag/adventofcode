require 'minitest/autorun'

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

def run_intcode(intcode, phase_setting, input_value)
  
  i = 0
  use_input_value = false
  loop do
  
    if i == intcode.length
      break
    end
    
    command = intcode[i]
    opcode = get_opcode_for_command(command.to_s)
       
    if opcode == :halt
      
      puts "End Program"
      # break
      
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
      if use_input_value
        read_value = input_value
      else
        read_value = phase_setting
      end
      use_input_value = true
      intcode[first_input_value] = read_value.to_s
      
    elsif opcode == :write
    
      first_input_index = Integer(intcode[i+1])
      return Integer(intcode[first_input_index])

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

def calculate_thrust(intcode, amplifiers)
  max_thrust = 0
  amplifiers.permutation { |amplifier_phase_order|
    input = 0
    for amplifier_phase in amplifier_phase_order do
      thrust = run_intcode(intcode, amplifier_phase, input.to_s)
      if thrust >= max_thrust
        max_thrust = thrust
      end
      input = thrust
    end
  }
  
  max_thrust
end

def calculate_super_thrust(intcode, amplifiers)
  max_thrust = 0
  amplifiers.permutation { |amplifier_phase_order|
    input = 0
    for amplifier_phase in amplifier_phase_order do
      thrust = run_intcode(intcode, amplifier_phase, input.to_s)
      if thrust >= max_thrust
        max_thrust = thrust
      end
      input += thrust
    end
  }
  
  max_thrust
end

def first_puzzle
  intcode = IO.read("AmplifierControllerSoftware.txt").split(",")
  puts "max threshold: #{calculate_thrust(intcode, [0,1,2,3,4])}"
end

class ThrustTests < MiniTest::Test
  def test_thrust_43210
    intcode = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")
    thrust = calculate_thrust(intcode, [0,1,2,3,4])
    assert_equal 43210, thrust
  end
  
  def test_thrust_54321
    intcode = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")
    thrust = calculate_thrust(intcode, [0,1,2,3,4])
    assert_equal 54321, thrust
  end
  
  def test_thrust_65210
    intcode = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")
    thrust = calculate_thrust(intcode, [0,1,2,3,4])
    assert_equal 65210, thrust
  end
  
  def test_super_thrust_139629729
    intcode = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")
    super_thrust = calculate_super_thrust(intcode, [5,6,7,8,9])
    assert_equal 139629729, super_thrust
  end

    def test_super_thrust_18216
    intcode = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(",")
    super_thrust = calculate_super_thrust(intcode, [5,6,7,8,9])
    assert_equal 18216, super_thrust
  end
end