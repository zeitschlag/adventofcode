require "minitest/autorun"

class ProgramTests < Minitest::Test
  
  def test_quine
    quine_code = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    intcode = quine_code.split(",")
    program = Program.new(intcode)
    program.run
    assert_equal quine_code, program.log.join(",")
  end
  
  def test_large_number_output
    intcode = "104,1125899906842624,99".split(",")
    program = Program.new(intcode)
    assert_equal "1125899906842624", program.run
  end
  
  def test_large_number
    intcode = "1102,34915192,34915192,7,4,7,99,0".split(",")
    program = Program.new(intcode)
    assert_equal 16, program.run.length
  end
end

class Program

  attr_reader :log
  
  POSITIONMODE = "0"
  IMMEDIATEMODE = "1"
  RELATIVEMODE = "2"

  def initialize(intcode)
    @relative_base = 0
    @intcode = intcode + Array.new(2_000_000, "0")
    @log = []
  end

  def get_first_parameter_value(command, index)
    input_index = Integer(@intcode[index+1])
    param_mode = command[-3]
  
    if param_mode == IMMEDIATEMODE
      Integer(input_index)
    elsif param_mode == RELATIVEMODE
      Integer(@intcode[input_index + @relative_base])
    elsif param_mode == POSITIONMODE || param_mode.nil?
      Integer(@intcode[input_index])
    end
  end

  def get_second_parameter_value(command, index)
    input_index = Integer(@intcode[index+2])
    param_mode = command[-4]
  
    if param_mode == IMMEDIATEMODE
      Integer(input_index)
    elsif param_mode == RELATIVEMODE
      Integer(@intcode[input_index + @relative_base])
    elsif param_mode == POSITIONMODE || param_mode.nil?
      Integer(@intcode[input_index])
    end
  end

  def get_third_parameter_value(command, index)
    Integer(@intcode[index+3])
  end

  def run()
    # add base
    current_index = 0
    status_code = 0
    
    loop do
    
      if current_index == @intcode.length
        break
      end
      
      command = @intcode[current_index]
      
      opcode = get_opcode_for_command(command.to_s)
         
      if opcode == :halt
        
        return status_code
        
      elsif opcode == :add
          
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        output_index = get_third_parameter_value(command, current_index)
        
        result = first_input_value + second_input_value
        @intcode[output_index] = result.to_s
        
      elsif opcode == :multiply
        
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        output_index = get_third_parameter_value(command, current_index)
        
        result = first_input_value * second_input_value
        @intcode[output_index] = result.to_s
        
      elsif opcode == :read
        
        first_input_value = get_first_parameter_value(command, current_index)
        @intcode[first_input_value] = "1" # first input value, this is a dirty hack
        
      elsif opcode == :write
        
        status_code = get_first_parameter_value(command, current_index).to_s
        @log.append(status_code)
        
      elsif opcode == :jump_if_true
        
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        
        if first_input_value != 0
          current_index = Integer(second_input_value)
          next
        end
        
      elsif opcode == :jump_if_false
        
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        
        if first_input_value == 0
          current_index = Integer(second_input_value)
          next
        end
        
      elsif opcode == :less_than
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        output_index = Integer(@intcode[current_index+3])
        
        if first_input_value < second_input_value
          @intcode[output_index] = "1"
        else
          @intcode[output_index] = "0"
        end
        
      elsif opcode == :equals
        first_input_value = get_first_parameter_value(command, current_index)
        second_input_value = get_second_parameter_value(command, current_index)
        output_index = Integer(@intcode[current_index+3])
        
        parameters_equal = first_input_value == second_input_value
        if parameters_equal
          @intcode[output_index] = "1"
        else
          @intcode[output_index] = "0"
        end
        
      elsif opcode == :adjust_relative_base
        first_input_value = get_first_parameter_value(command, current_index)
        @relative_base += first_input_value
      else
        raise "Weird opcode (#{opcode} at #{i}), command: #{command}, aborting..."
      end
      
      number_of_parameters = number_of_parameters_for_opcode(opcode)
      
      current_index += number_of_parameters
      current_index += 1 # next command
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
    elsif command.end_with?("9")
      :adjust_relative_base
    end
  end
  
  def number_of_parameters_for_opcode(opcode)
    if opcode == :halt
      0
    elsif opcode == :add || opcode == :multiply || opcode == :less_than || opcode == :equals
      3
    elsif opcode == :jump_if_false || opcode == :jump_if_true
      2
    elsif opcode == :read || opcode == :write || opcode == :adjust_relative_base
      1
    end
  end
end

def first_puzzle 
  intcode = IO.read("BOOST.txt").split(",")
  program = Program.new(intcode)
  program.run
  puts "Log: #{program.log}"
end

first_puzzle
