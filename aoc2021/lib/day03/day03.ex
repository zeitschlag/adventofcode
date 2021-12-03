defmodule AoC2021.Day03 do
  def part01 do
    report_numbers = read("input.txt")

    gamma = calculate_gamma_rate(report_numbers)
    epsilon = calculate_epsilon_rate(report_numbers)

    power_consumption(gamma, epsilon)
  end

  def read(input) do
    {:ok, content} = File.read(input)

    String.split(content, "\n")
  end

  def calculate_gamma_rate(report_numbers) when is_list(report_numbers) do
    calculate_rate(report_numbers, :gamma)
  end

  def calculate_epsilon_rate(report_numbers) when is_list(report_numbers) do
    calculate_rate(report_numbers, :epsilon)
  end

  defp calculate_rate(report_numbers, rating) when is_list(report_numbers) do
    report_numbers
    |> Enum.map(&String.graphemes/1)
    |> List.zip()
    |> Enum.map(fn list -> get_rate(Tuple.to_list(list), rating) end)
    |> Enum.join()
    |> String.to_integer(2)
  end

  defp get_rate(list, rating) do
    case rating do
      :epsilon -> least_common_bit(list)
      :gamma -> most_common_bit(list)
    end
  end

  def least_common_bit(list) do
    common_bit(:least, list)
  end

  def most_common_bit(list) do
    common_bit(:most, list)
  end
  
  defp common_bit(type, list) do
    number_of_zeros = Enum.count(list, fn elem -> elem == "0" end)
    number_of_ones = Enum.count(list, fn elem -> elem == "1" end)
    
    more_zeros = number_of_zeros > number_of_ones

    if more_zeros do
      case type do
        :most -> 0
        :least -> 1
      end
    else
      case type do
        :most -> 1
        :least -> 0
      end
    end
    
  end

  def power_consumption(gamma_rate, epsilon_rate)
      when is_integer(gamma_rate) and is_integer(epsilon_rate) do
    gamma_rate * epsilon_rate
  end
end
