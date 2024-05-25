import numpy
numpy.set_printoptions(legacy='1.13')

array_a = list(map(float, input().split()))
# print(type(array_a))

#Convert list into numpy array:
array_a = numpy.array(array_a)
# print(type(array_a))

print(numpy.floor(array_a))
print(numpy.ceil(array_a))
print(numpy.rint(array_a))

# # INPUT:
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

#--------Yashvi Bhadania--------