defmodule Day01Tests do
  use ExUnit.Case
  import AoC2021.Day01, only: [ count_increases: 1 ]

  test "count 7 encreased" do
    input = [ 199, 200, 208, 210, 200, 207, 240, 269, 260, 263 ]
    assert count_increases(input) == 7
  end
end
