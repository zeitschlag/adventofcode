# read the list twice
# double-iterate over those two lists
# if a+b == 2020:
  # calculate a*b

expense_list = open("input.txt", "r").readlines()

for a in expense_list:
    for b in expense_list:
        for c in expense_list:
            sum = int(a)+int(b)+int(c)

            if sum==2020:
                result = int(a)*int(b)*int(c)
                print("{a}*{b}*{c}={result}".format(a=a.strip(), b=b.strip(), c=c.strip(), result=str(result)))
                exit()
