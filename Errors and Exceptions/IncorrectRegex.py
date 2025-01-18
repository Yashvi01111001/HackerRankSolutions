# # Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    try:
        a = (re.compile(input()))
        print(bool(a))
    except re.error:
        print('False') 

# # SAMPLE INPUT:
# 2
# .*\+
# .*+

#--------Yashvi Bhadania--------
