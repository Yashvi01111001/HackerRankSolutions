# SRC: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

# Read input values
AB = int(input())
BC = int(input())

# Calculate the angle in radians
theta_radians = math.atan2(AB, BC)

# Convert the angle to degrees
theta_degrees = math.degrees(theta_radians)

# Round the angle to the nearest integer
theta_degrees_rounded = round(theta_degrees)

# Print the angle with the degree symbol
print(f"{theta_degrees_rounded}{chr(176)}")

# # SAMPLE INPUT:
# 10
# 10

#--------Yashvi Bhadania--------