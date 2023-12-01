defmodule AoC2023 do
  def read(input) do
    {:ok, content} = File.read(input)

    String.split(content, "\n")
  end
end
