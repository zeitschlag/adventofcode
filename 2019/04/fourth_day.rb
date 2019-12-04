
def is_number_potential_password?(number)
  # has six digits
  has_six_digits = number.to_s.length == 6
  # two adjacent digits are the same
  two_adjacent_digits = false
  number_string = number.to_s
  
  number_string.chars.each_cons(2) { |two_digits|
  	if two_digits[0] == two_digits[1]
  	  two_adjacent_digits = true
  	end
  }

  # digits never decrease. Sort and compare if strings are the same
  never_decrease = number.to_s.chars.sort == number.to_s.chars

  return (has_six_digits && never_decrease && two_adjacent_digits)
end

def first_puzzle

  potential_passwords = []

  (353096..843212).each { |current_number|
  	if is_number_potential_password?(current_number)
	  potential_passwords.append(current_number)
	end
  }
  
  puts "Potential Passwords: #{potential_passwords.length}"
end

first_puzzle
