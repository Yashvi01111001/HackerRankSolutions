# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

S, k = list(input().split())

k = int(k)

result = []
for i in range(1, k+1):
    result.extend(combinations(sorted(S), i))
print(result)

for j in result:
    print(''.join(j))
    
# NOTE:
# append() adds its argument as a single element, regardless of whether the argument is an individual item or a list.
# extend() takes an iterable (list, string, tuple, etc.) and adds each element of the iterable to the list.

# # SAMPLE INPUT:
# HACK 2

#--------Yashvi Bhadania--------