defmodule Day01Tests do
  use ExUnit.Case
  import AoC2021.Day01, only: [count_increases: 1, count_increases_in_windows: 1]

  test "count 7 encreased" do
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert count_increases(input) == 7
  end

  test "count 5 encreased using windoes" do
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert count_increases_in_windows(input) == 5
  end
end
