x = 1
y = 1
z = 1
n = 2

result = [] 
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            perm_list = [i,j,k]
            # print(perm_list) 
            list_sum = sum(perm_list)#calculating sum of each list:
            # print(list_sum)
            if list_sum != n:
                # print(perm_list, end=" ")
                # print(type(perm_list))
                result.append(perm_list)
print(result)


# Let's break down the logic for the permutation for loops with range:

# The outermost loop for i in range(x+1) iterates over all possible values of i from 0 to x, inclusive.
# For each value of i, the middle loop for j in range(y+1) iterates over all possible values of j from 0 to y, inclusive.
# For each combination of i and j, the innermost loop for k in range(z+1) iterates over all possible values of k from 0 to z, inclusive.Let's break down the logic:

# The outermost loop for i in range(x+1) iterates over all possible values of i from 0 to x, inclusive.
# For each value of i, the middle loop for j in range(y+1) iterates over all possible values of j from 0 to y, inclusive.
# For each combination of i and j, the innermost loop for k in range(z+1) iterates over all possible values of k from 0 to z, inclusive.

# i = 0, j = 0, k = 0
# i = 0, j = 0, k = 1
# i = 0, j = 1, k = 0
# i = 0, j = 1, k = 1
# i = 1, j = 0, k = 0
# i = 1, j = 0, k = 1
# i = 1, j = 1, k = 0
# i = 1, j = 1, k = 1

# # INPUT:
# 1
# 1
# 1
# 2

#--------Yashvi Bhadania--------
