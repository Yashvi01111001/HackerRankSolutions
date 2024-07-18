# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
my_list1 = list(map(int, input().split()))
my_set1 = set(my_list1)
# print(my_set1)

# Iterating over the set to remove one instance of every number from the list
for _ in my_set1:
    my_list1.remove(_)
# print(my_list)

# Converting the list to a set to use difference(), removes duplicates too
my_set2 = set(my_list1)
# print(my_set2)

# Then, comparing both sets
result = my_set1.difference(my_set2)
# Converting result in set into a list
result = list(result)
# To print, we access the first element in the list (our answer)
print(result[0])

# # INPUT:
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

#--------Yashvi Bhadania--------