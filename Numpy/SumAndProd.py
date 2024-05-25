import numpy

# #NOTES (IN THE CASE OF ADDITION):
# #axis=0 adds up the columns
# #axis=1 adds up the rows
# #axis=None adds up all the elements (all rows + all columns)

N, M = list(map(int, input().split()))
my_array = [[int(i) for i in input().split()]for x in range(N)]
my_array = numpy.sum(my_array, axis=0)
print(numpy.prod(my_array))

# # INPUT:
# 2 2
# 1 2
# 3 4

#--------Yashvi Bhadania--------