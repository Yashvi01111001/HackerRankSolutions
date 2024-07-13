# Some extra info here :)
# The intersection operator (&) only allows sets as parameters.
# While the intersection method (intersection()) can accept any type of 
# iterables such as lists, strings, dictionaries...

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

intersection_res = english.intersection(french)

intersection_res = len(intersection_res)

print(intersection_res)

# # INPUT:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

#--------Yashvi Bhadania--------