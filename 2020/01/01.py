# read the list twice
# double-iterate over those two lists
# if a+b == 2020:
  # calculate a*b

expense_list = open("input.txt", "r").readlines()

for a in expense_list:
    for b in expense_list:
        sum = int(a)+int(b)

        if sum==2020:
            result = int(a)*int(b)
            print("{a}*{b}={result}".format(a=a.strip(), b=b.strip(), result=str(result)))
            exit()
