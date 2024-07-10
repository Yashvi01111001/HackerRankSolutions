# Enter your code here. Read input from STDIN. Print output to STDOUT

en = int(input())
en_set = set(map(int, input().split()))
fr = int(input())
fr_set = set(map(int, input().split()))

diff = en_set.difference(fr_set)

print(len(diff))

# # INPUT:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

#--------Yashvi Bhadania--------
