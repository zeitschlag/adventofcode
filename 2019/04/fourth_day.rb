potential_passwords = []

(353096..843212).each { |current_number|
  # has six digits
  has_six_digits = current_number.to_s.length == 6
  # two adjacent digits are the same
  two_adjacent_digits = false
  number_string = current_number.to_s
  if number_string[0] == number_string[1] || number_string[1] == number_string[2] || number_string[2] == number_string[3] || number_string[3] == number_string[4] || number_string[4] == number_string[5]
    two_adjacent_digits = true
  end
  # digits never decrease. Sort and compare if strings are the same
  never_decrease = current_number.to_s.chars.sort == current_number.to_s.chars

  if has_six_digits && never_decrease && two_adjacent_digits
    potential_passwords.append(current_number)
  end
}

puts "Potential Passwords: #{potential_passwords.length}"
