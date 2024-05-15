import numpy

n = int(input())

# Initialize an empty list to store the matrix
matrix = []

# Use nested list comprehension to create the matrix
for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)
# print(matrix)

#Finding the determinant:
det_result = numpy.linalg.det(matrix)
# print(det_result)
rounded_det_result = round(det_result, 2)
print(rounded_det_result)

#--------Yashvi Bhadania--------