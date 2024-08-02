# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

S, k = list(input().split())

S = list(S)
S.sort()
S = ''.join(S)
# print(S)

result = list(permutations(S, int(k)))

for _ in result:
    print(''.join(_))

# # SAMPLE INPUT:
# HACK 2

#--------Yashvi Bhadania--------