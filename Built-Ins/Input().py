# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
P = input()
# print(P)
P = P.replace('x', str(x))
P_result = eval(P)
print(P_result==k)

# # SAMPLE INPUT:
# 1 4
# x**3 + x**2 + x + 1
#--------Yashvi Bhadania--------
