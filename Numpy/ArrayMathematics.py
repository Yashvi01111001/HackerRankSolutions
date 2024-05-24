import numpy

N, M = map(int, input().split()) #N is row, M is column

A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]
# print(type(A))


#Converting type to array
A = numpy.array(A)
B = numpy.array(B)
# print(type(A))


sum_result = numpy.add(A, B)

diff = numpy.subtract(A, B)

prod = numpy.multiply(A, B)

quotient = numpy.floor_divide(A, B)
    
remainder = numpy.mod(A, B)

power = numpy.power(A, B)

print(sum_result, diff, prod, quotient, remainder, power, sep="\n")

# # INPUT:
# 1 4
# 1 2 3 4
# 5 6 7 8

#--------Yashvi Bhadania--------