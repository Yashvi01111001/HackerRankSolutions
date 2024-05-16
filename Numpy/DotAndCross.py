import numpy as np

# Read the size of the matrix (N)
N = int(input())

# Initialize the matrices to multiply
matrix1 = []
matrix2 = []

# Read the first matrix
for _ in range(N):
    rows = list(map(int, input().split()))  # Convert input strings to floats
    matrix1.append(rows)

# Read the second matrix
for _ in range(N):
    rows = list(map(int, input().split()))  # Convert input strings to floats
    matrix2.append(rows)

# Convert lists to NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Multiply matrices using numpy dot function
result = np.dot(matrix1, matrix2)
print(result)

# INPUT:
# 2
# 1 2
# 3 4
# 1 2
# 3 4

#--------Yashvi Bhadania--------