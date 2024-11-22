# SRC: https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

S = input()

# Use groupby to group consecutive characters
result = []
for char, group in groupby(S):
    # print(char)
    # print(list(group))
    count = len(list(group))  # Count the number of occurrences
    result.append(f"({count}, {char})")

# Join the results with a space and print
print(" ".join(result))

# SAMPLE INPUT:

# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 

#--------Yashvi Bhadania--------