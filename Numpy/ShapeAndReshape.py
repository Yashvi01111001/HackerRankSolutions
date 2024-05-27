import numpy

my_array = list(map(int, input().split()))

#Using .shape
my_array = numpy.array(my_array)
my_array.shape = (3,3)
print(my_array)

# #or using .reshape
# print(numpy.reshape(my_array, (3,3)))

# # INPUT:
# 1 2 3 4 5 6 7 8 9

#--------Yashvi Bhadania--------