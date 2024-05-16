import numpy

matrix = []

for _ in range(2):
    rows = list(map(int, input().split()))
    matrix.append(rows)

# print(matrix)
inner_prod_result = numpy.inner(matrix[0], matrix[1])
print(inner_prod_result)
outer_prod_result = numpy.outer(matrix[0], matrix[1])
print(outer_prod_result)


#--------Yashvi Bhadania--------