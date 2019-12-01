def calculate_fuel(module_mass)
  module_fuel = (module_mass.to_f/3).floor - 2
  return module_fuel
end

required_fuel = 0

File.open("input.txt", "r") do |file|
  file.each_line do |module_mass|
    required_fuel += calculate_fuel(module_mass)
  end
end

puts required_fuel


