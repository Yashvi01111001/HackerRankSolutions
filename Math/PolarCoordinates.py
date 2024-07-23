# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

complex_num = complex(input())

# Getting polar coordinates individually i.e. r = abs() and theta = phase()
# r = abs(complex_num) # calculates the euclidean distance
# theta = cmath.phase(complex_num)

# Alternatively, get polar coordinates directly
r, theta = cmath.polar(complex_num)

# Print the results
print(r)
print(theta)


# # SAMPLE INPUT:
# 1+2j

#--------Yashvi Bhadania--------