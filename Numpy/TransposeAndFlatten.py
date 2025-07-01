import numpy

N, M = list(map(int, input().split()))

my_array = [[int(i) for i in input().split()] for x in range(N)]
# print(my_array)

#transposing array
print(numpy.transpose(my_array))

#flattening array
my_array = numpy.array(my_array)
print(my_array.flatten())

# # SAMPLE INPUT:
# 2 2
# 1 2
# 3 4

#--------Yashvi Bhadania--------
