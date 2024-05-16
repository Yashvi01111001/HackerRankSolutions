import numpy
matrix = []

#Getting values for N and M from space separated user input
N, M = map(int, input().split())
# print(N, M)

for _ in range(N):
    row = list(map(float, input().split()))
    # print(row)
    matrix.append(row)
# print(matrix) #now we've gotten the input in the desired format to pass it to the numpy functions, i.e. nested list

mean_result = numpy.mean(matrix, axis=1)
var_result = numpy.var(matrix, axis=0)
std_result = numpy.std(matrix, axis=None)
std_result = round(std_result, 11)
print(mean_result)
print(var_result)
print(std_result)

# # INPUT:
# 2 2
# 1 2
# 3 4

#--------Yashvi Bhadania--------