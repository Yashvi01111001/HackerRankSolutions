T = int(input())
for _ in range(T):
    nSetA = int(input())
    setA = set(map(int, input().split()))
    nSetB = int(input())
    setB = set(map(int, input().split()))
    
    if setA.intersection(setB) == setA:
        print(True)
    else:
        print(False)
        
# # INPUT:
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

#--------Yashvi Bhadania--------