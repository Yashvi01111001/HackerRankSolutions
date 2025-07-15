# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()

# Finding all matches:
matches = list(re.finditer(rf'(?={re.escape(k)})', s))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))

# # SAMPLE INPUT:
# aaadaa
# aa

#--------Yashvi Bhadania--------