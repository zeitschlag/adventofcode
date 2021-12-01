defmodule AoC2021.Day01 do
  def count_increases(input) do
    Enum.chunk_every(input, 2, 1, :discard)
    |> Enum.count(fn list -> Enum.sort(list) == list end)
  end

  def part01(input) do
    IO.puts(count_increases(input))
  end
end
