def calculate_fuel(module_mass)
  module_fuel = (module_mass.to_f/3).floor - 2
  return module_fuel
end

def calculate_total_fuel(mass)
  fuel = calculate_fuel(mass)
  additional_fuel = calculate_fuel(fuel)

  while additional_fuel >= 0 do
    fuel += additional_fuel
    additional_fuel = calculate_fuel(additional_fuel)
  end

  return fuel
end

required_fuel = 0

File.open("input.txt", "r") do |file|
  file.each_line do |module_mass|
    required_fuel += calculate_total_fuel(module_mass)
  end
end

puts required_fuel


