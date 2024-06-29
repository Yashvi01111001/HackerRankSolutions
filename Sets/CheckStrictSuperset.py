# SRC: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

# FYI:
# The proper superset is also known as a strict superset. The set B is the proper superset of set A, then all the elements of set A are in B, but set B must contain at least one element which is not present in set A

setA = set(map(int, input().split()))
n = int(input())
result = []
for _ in range(n):
    setB = set(map(int, input().split()))
    diff = setA.difference(setB)

    if setB.intersection(setA) == setB:
        if bool(diff & setB) == False:
            result.append(True)
    else:
        result.append(False)

# print(result)
if False in result:
    print(False)
else:
    print(True)

# # INPUT:
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

#--------Yashvi Bhadania--------
