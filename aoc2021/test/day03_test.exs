defmodule Day03Tests do
  use ExUnit.Case

  import AoC2021.Day03, only: [power_consumption: 2, most_common_bit: 1, least_common_bit: 1, calculate_gamma_rate: 1, calculate_epsilon_rate: 1]

  test "more ones than zeros" do
    assert most_common_bit(["1", "1", "0"]) == 1
  end

  test "less ones than zeros" do
    assert least_common_bit(["1", "1", "0"]) == 0
  end

  test "power consumption = 14 * 10" do
    gamma_rate = 14
    epsilon_rate = 10

    assert power_consumption(gamma_rate, epsilon_rate) == 140
  end

  test "calculate gamma from binary-string" do
    report_numbers = ["00100", "11110", "11100"]
    assert calculate_gamma_rate(report_numbers) == 28
  end
 
  test "calculate epsilon from binary-string" do
    report_numbers = ["00100", "11110", "11100"]
    assert calculate_epsilon_rate(report_numbers) == 3
  end
end
