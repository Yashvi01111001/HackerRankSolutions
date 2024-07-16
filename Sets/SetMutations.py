# Enter your code here. Read input from STDIN. Print output to STDOUT

n_setA = int(input())
setA = set(map(int, input().split()))
n_other_sets = int(input())

for _ in range(n_other_sets):
    operation, N = list(input().split())
    elements = list(map(int, input().split()))

    if operation == "intersection_update":
        setA.intersection_update(elements)
        # print(setA)
    if operation == "update":
        setA.update(elements)
        
    if operation == "symmetric_difference_update":
        setA.symmetric_difference_update(elements)
        
    if operation == "difference_update":
        setA.difference_update(elements)
        
# print(setA)
print(sum(setA))

# # INPUT:
#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66

#--------Yashvi Bhadania--------