#SRC: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true 

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))

union_res = english.union(french)

res = len(union_res)
print(res)

# # INPUT:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

#--------Yashvi Bhadania--------