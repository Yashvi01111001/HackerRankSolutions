# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = list(input().split())

result = list(combinations_with_replacement(sorted(S), int(k)))

for _ in result:
    print(''.join(_))

# # SAMPLE INPUT:
# HACK 2

#--------Yashvi Bhadania--------