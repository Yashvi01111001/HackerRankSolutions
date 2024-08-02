# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

# Reading the input lists
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Generating the Cartesian product
result = product(a, b)

# Use the unpacking operator * to print each tuple in the Cartesian product, separated by a space.
print(*result)

# # SAMPLE INPUT:
#  1 2
#  3 4

#--------Yashvi Bhadania--------