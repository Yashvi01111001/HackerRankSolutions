#!/bin/python3
 
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    # print(arr)
    # k_column_values = []
    # for _ in arr:
    #     k_column_values.append(_[k])
    # k_column_values = sorted(k_column_values)
    
    # for x in k_column_values:
    #     for _ in arr:
    #         if _[k]==x:
    #             print(*_)
    # THE ABOVE CODE DID NOT PASS TEST CASE 2 WHICH REQUIRED MAINTAINING INPUT ORDER
    
    # Sort the array using a lambda function as the key
    
    # arr.sort(): This is the built-in sort() method for lists in Python. It sorts the list in place, meaning it modifies the original list directly.
    
    # LAMBDA FORMAT: lambda arguments: expression
    # lambda row: row[k] means:
    # lambda row: Define a lambda function that takes one argument named row.
    # row[k]: The expression that the function evaluates and returns. It accesses the element at index k of the row list.
    arr.sort(key=lambda row: row[k])

    for row in arr:
        print(*row)

# # SAMPLE INPUT:
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

#--------Yashvi Bhadania--------