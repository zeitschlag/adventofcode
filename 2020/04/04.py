def read_documents(filename: str):
    raw_input = open(filename, "r").read()
    return raw_input.split("\n\n")


def is_valid_document(document: str):
    has_birthyear = "byr:" in document
    has_issueyear = "iyr:" in document
    has_expirationyear = "eyr:" in document
    has_height = "hgt:" in document
    has_haircolor = "hcl:" in document
    has_eyecolor = "ecl:" in document
    has_passport_id = "pid:" in document

    return has_birthyear & has_issueyear & has_expirationyear & has_height & has_haircolor & has_eyecolor & has_passport_id


if __name__ == '__main__':

    documents = read_documents(filename="passport_list.txt")
    valid_document_counter = 0

    for document in documents:
        if is_valid_document(document=document):
            valid_document_counter += 1

    print("Number of valid documents: {0}".format(valid_document_counter))