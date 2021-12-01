defmodule AoC2021.Day01 do
  def count_increases(input) do
    Enum.chunk_every(input, 2, 1, :discard)
    |> Enum.count(fn list -> Enum.sort(list) == list end)
  end

  def count_increases_in_windows(input) do
    sums = Enum.chunk_every(input, 3, 1, :discard)
    |> Enum.map(&Enum.sum/1)

    Enum.chunk_every(sums, 2, 1, :discard)
    |> Enum.count(fn [a, b] -> Enum.sort([a, b]) == [a, b] and a != b end)
  end

  def part01(input) do
    IO.puts(count_increases(input))
  end

  def part02(input) do
    IO.puts count_increases_in_windows(input)
  end
end
