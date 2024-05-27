import numpy

N, M, P = list(map(int, input().split()))

array_a = [[int(i) for i in input().split()] for x in range(N)]
# print(array_a)

array_b = [[int(i) for i in input().split()] for x in range(M)]
# print(array_b)

print(numpy.concatenate((array_a, array_b)))


# # INPUT:
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 

#--------Yashvi Bhadania--------