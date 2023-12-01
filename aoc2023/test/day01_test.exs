defmodule AoC2023Test.DayOne do

  use ExUnit.Case
  
  test "Parse line" do
    expected = 12
    result = AoC2023.DayOne.parse_line("1abc2")
    
    assert expected == result
  
  end
  
  test "Run example" do

    expected = 142
    result = "test/day_one_1.txt"
    |> AoC2023.DayOne.part_one()
    
    assert expected == result

  end
  
end