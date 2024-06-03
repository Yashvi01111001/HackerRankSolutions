#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return re.sub(r'\b\w', lambda match: match.group().upper(), s)

#     re.sub(): This function is used to perform a substitution operation on a string using a regular expression pattern.
# r'\b\w': This regular expression pattern matches the beginning of each word (\b word boundary) followed by a word character (\w).
# lambda match: match.group().upper(): This lambda function is applied to each match found by the regular expression. It takes a match object as input and returns the uppercase version of the matched substring using match.group().upper().
# s: This is the input string containing the full name.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# # INPUT:
# yashvi bhadania

#--------Yashvi Bhadania--------