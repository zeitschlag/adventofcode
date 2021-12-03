defmodule AoC2021.Day02 do
  defmodule Part01 do
    def calculate_position(depth, h_pos) do
      depth * h_pos
    end

    def solve(input) do
      final_pos =
        parse(input)
        |> run

      calculate_position(final_pos.depth, final_pos.h_pos)
    end

    def parse(filename) do
      {:ok, content} = File.read(filename)

      String.split(content, "\n")
      |> Enum.map(fn str -> String.split(str) end)
      |> Enum.map(fn [direction, delta] ->
        %{:direction => String.to_atom(direction), :delta => String.to_integer(delta)}
      end)
    end

    def run(instructions) do
      Enum.reduce(instructions, %{:depth => 0, :h_pos => 0}, fn instr, param ->
        run(instr, param)
      end)
    end

    def run(instruction, param) do
      depth = param.depth
      h_pos = param.h_pos
      delta = instruction.delta

      case instruction.direction do
        :forward -> forward(delta, depth, h_pos)
        :up -> up(delta, depth, h_pos)
        :down -> down(delta, depth, h_pos)
      end
    end

    def forward(delta, depth, h_pos) do
      %{:depth => depth, :h_pos => h_pos + delta}
    end

    def up(delta, depth, h_pos) do
      %{:depth => depth - delta, :h_pos => h_pos}
    end

    def down(delta, depth, h_pos) do
      %{:depth => depth + delta, :h_pos => h_pos}
    end
  end
  
  defmodule Part02 do
    def calculate_position(depth, h_pos) do
      depth * h_pos
    end

    def solve(input) do
      final_pos =
        parse(input)
        |> run

      calculate_position(final_pos.depth, final_pos.h_pos)
    end

    def parse(filename) do
      # todo: read file, make instructions-map with atoms and int
      {:ok, content} = File.read(filename)

      String.split(content, "\n")
      |> Enum.map(fn str -> String.split(str) end)
      |> Enum.map(fn [direction, delta] ->
        %{:direction => String.to_atom(direction), :delta => String.to_integer(delta)}
      end)
    end

    def run(instructions) do
      # follow instructions aka do some magic
      # returns %{"depth" => 10, "h_pos" => 15}
      # instructions
      # |> run(depth, h_pos)
      Enum.reduce(instructions, %{:depth => 0, :h_pos => 0, :aim => 0}, fn instr, param ->
        run(instr, param)
      end)
    end

    def run(instruction, param) do
      # instruction = direction and delta
      # follow instruction and modify either depth or h_pos
      depth = param.depth
      h_pos = param.h_pos
      aim = param.aim
      delta = instruction.delta

      case instruction.direction do
        :forward -> forward(delta, depth, h_pos, aim)
        :up -> up(delta, depth, h_pos, aim)
        :down -> down(delta, depth, h_pos, aim)
      end
    end

    def forward(delta, depth, h_pos, aim) do
      %{:depth => depth + aim * delta, :h_pos => h_pos + delta, :aim => aim}
    end

    def up(delta, depth, h_pos, aim) do
      %{:depth => depth, :h_pos => h_pos, :aim => aim - delta}
    end

    def down(delta, depth, h_pos, aim) do
      %{:depth => depth, :h_pos => h_pos, :aim => aim + delta}
    end
  end
end
