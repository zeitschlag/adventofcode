input = 353096..843212

# find out, how many strings from 353096-843212 are potential passwords
# Criteria:
# 6 digits (all of them)
# two adjacent digits are the same
# digits never decrease, but increase or stay the sam
#
# plan:
# iterate over all possible input-strings
# check for criteria. if one fails: next string
