import numpy

N, M = list(map(int, input().split()))

my_array = [[int(i) for i in input().split()] for x in range(N)]

min_result = numpy.min(my_array, axis=1) 

print(numpy.max(min_result))

# # INPUT:
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

#--------Yashvi Bhadania--------