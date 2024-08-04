# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

N = int(input())
elems = input().split()
K = int(input())

combinations_tuple = tuple(combinations(elems, K))

count = 0
numerator = 0

for _ in combinations_tuple:
    count += 1
    if "a" in _:
        numerator += 1

result = numerator/count
print(result)

# # SAMPLE INPUT:
# 4 
# a a c d
# 2

#--------Yashvi Bhadania--------