import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    # print(arr)
    arr.reverse()
    # print(rev_array)
    arr = numpy.array(arr, float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# # INPUT:
# 1 2 3 4 -8 -10

#--------Yashvi Bhadania--------