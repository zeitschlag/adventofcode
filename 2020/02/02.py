# repeat for every line
#   1. split with :, first part is rule, second part is password
#   2. split rule at space: first part is amount (split again for min/max), second part is character
#   3. check if character appears between min/max times in password aka min < str.count(character) < max

def valid_password(password: str, character: str, minimum: int, maximum: int):
    number_chars = password.count(character)
    valid = (int(minimum) <= number_chars <= int(maximum))

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
    minimum = amounts[0]
    maximum = amounts[1]

    password_is_valid = valid_password(password, character, int(minimum), int(maximum))
    if password_is_valid:
        valid_passwords += 1

print("Valid passwords: "+ str(valid_passwords))

