import numpy
numpy.set_printoptions(legacy='1.13') #to get the alignment correct

N, M = map(int, input().split())

print(numpy.eye(N, M))