import numpy

coefficients = list(map(float, input().split()))
# print(coefficients)

x_value = int(input())
# print(x_value)

n = len(coefficients)-1 #the powers of x
# print(n)
idx = 0 #index of the coefficients list
sum = 0
while n>-1:
    # print(n)
    results = coefficients[idx]*(x_value)**n
    sum += results
    n-=1
    idx += 1
print(sum)

# # INPUT:
# 1.1 2 3
# 0

#--------Yashvi Bhadania--------