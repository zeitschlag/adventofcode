# read input-file
input_file = open("input", "r")
input_file_content = input_file.read()
lines = input_file_content.split("\n")

result = 0

for line in lines:
    if line is not '':
        result = result + int(line)

print(result)
