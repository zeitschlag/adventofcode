defmodule Day02Test do
  use ExUnit.Case
  import AoC2021.Day02, only: [calculate_position: 2, forward: 3, up: 3, down: 3, run: 1, run: 2]

  test "calculate end result with 10 and 15" do
    horizontal_position = 15
    depth = 10
    assert calculate_position(depth, horizontal_position) == 150
  end

  test "up instruction with h_pos 0 and depth 10" do
    h_pos = 0
    depth = 10
    assert up(5, depth, h_pos) == %{:depth => depth - 5, :h_pos => h_pos}
  end

  test "down instruction with h_pos 0 and depth 10" do
    h_pos = 0
    depth = 10
    assert down(5, depth, h_pos) == %{:depth => depth + 5, :h_pos => h_pos}
  end

  test "forward instruction with h_pos 0 and depth 10" do
    h_pos = 0
    depth = 10
    assert forward(5, depth, h_pos) == %{:depth => depth, :h_pos => 5}
  end

  test "run example instruction" do
    instr = %{ :direction => :forward, :delta => 20 }
    param = %{ :depth => 0, :h_pos => 0 }

    assert run(instr, param) == %{ :depth => 0, :h_pos => 20  }
  end

  test "follow example instructions" do
    instructions = [ %{:direction => :forward, :delta  =>  5}, %{:direction => :down, :delta => 5}, %{:direction => :forward, :delta => 8}, %{:direction => :up, :delta => 3}, %{:direction => :down, :delta => 8}, %{:direction => :forward, :delta => 2} ]
    assert run(instructions) == %{:depth => 10, :h_pos => 15}
  end
end
