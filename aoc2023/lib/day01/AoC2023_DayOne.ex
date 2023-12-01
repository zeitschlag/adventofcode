defmodule AoC2023.DayOne do
  # > The newly-improved calibration document consists of lines of text; 
  # > each line originally contained a specific calibration value that the Elves now
  # > need to recover. On each line, the calibration value can be found by combining 
  # > the first digit and the last digit (in that order) to form a single two-digit 
  # > number.
  def part_one(input) do
    AoC2023.read(input)
    |> Enum.filter(&(String.length(&1) != 0))
    |> Enum.map(&parse_line/1)
    |> Enum.sum()
  end
  
  def parse_line(line) do
    numbers =
      line
      |> String.graphemes()
      |> Enum.filter(fn char ->
        # see https://hexdocs.pm/elixir/Enum.html#flat_map/2
        case Integer.parse(char) do
          {_int, _rest} -> true
          :error -> false
        end
      end)

    first_integer = List.first(numbers)
    last_integer = List.last(numbers)

    String.to_integer("#{first_integer}#{last_integer}")
  end
end
