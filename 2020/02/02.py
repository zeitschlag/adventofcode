# repeat for every line
#   1. split with :, first part is rule, second part is password
#   2. split rule at space: first part is amount (split again for min/max), second part is character
#   3. check if character is either password[minimum+1] or password[maximum+1], but not both

def valid_password(password: str, character: str, first_position: int, second_position: int):

    first = password[first_position-1]
    second = password[second_position-1]

    valid = (first == character) ^ (second == character)

    return valid

password_entries = open("passwords.txt", "r").readlines()

valid_passwords = 0
for password_entry in password_entries:
    elements = password_entry.split(":")
    raw_rule = elements[0].strip()
    password = elements[1].strip()

    rule = raw_rule.split(" ")
    raw_amounts = rule[0].strip()
    character = rule[1].strip()
    amounts = raw_amounts.split("-")
    first_position = amounts[0]
    second_position = amounts[1]

    password_is_valid = valid_password(password, character, int(first_position), int(second_position))
    if password_is_valid:
        valid_passwords += 1

print("Valid passwords: {0}".format(valid_passwords))

