def read_documents(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n\n")


def is_valid_document(document: str):

    passport_entries = document.split()

    valid_birthyear = False
    valid_issueyear = False
    valid_expirationyear = False
    valid_height = False
    valid_haircolor = False
    valid_eyecolor = False
    valid_passport_id = False

    for passport_entry in passport_entries:
        key, value = passport_entry.split(":")

        if key == "byr":
            valid_birthyear = (len(value) == 4) & (int(value) >= 1920) & (int(value) <= 2002)
        elif key == "iyr":
            valid_issueyear = (len(value) == 4) & (int(value) >= 2010) & (int(value) <= 2020)
        elif key == "eyr":
            valid_expirationyear = (len(value) == 4) & (int(value) >= 2020) & (int(value) <= 2030)
        elif key == "hgt":

            if "cm" in value:
            # If cm, the number must be at least 150 and at most 193.
                height = value[:-2]
                valid_height = 150 <= int(height) <= 193

            elif "in" in value:
            # If in, the number must be at least 59 and at most 76.
                height = value[:-2]
                valid_height = 59 <= int(height) <= 76

        elif key == "hcl":
            try:
                valid_haircolor = (value[0] == "#") & (len(value) == 7) & (int(value[1:], 16) > 0)
            except:
                valid_haircolor = False
        elif key == "ecl":
            valid_eyecolor = value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]
        elif key == "pid":
             try:
                valid_passport_id = (len(value) == 9) & (int(value, 10) < 1000000000)
             except:
                 valid_passport_id = False

    return valid_birthyear & valid_issueyear & valid_expirationyear & valid_height & valid_haircolor & valid_eyecolor & valid_passport_id


if __name__ == '__main__':

    documents = read_documents(filename="passport_list.txt")
    valid_document_counter = 0

    for document in documents:
        if is_valid_document(document=document):
            valid_document_counter += 1

    print("Number of valid documents: {0}".format(valid_document_counter))