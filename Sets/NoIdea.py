# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = list(map(int, input().split()))
my_array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in my_array:
    if i in A:
        happiness += 1
      
    if i in B:
        happiness -= 1
print(happiness)


# # INPUT:
# 3 2
# 1 5 3
# 3 1
# 5 7

#--------Yashvi Bhadania--------
