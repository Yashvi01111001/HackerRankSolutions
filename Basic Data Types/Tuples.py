n = int(input())
integer_list = map(int, input().split())
# print(integer_list)
integer_tuple = tuple(integer_list)
# print(integer_tuple)
result = hash(integer_tuple)
print(result)

# NOTE: under the 'Language' dropdown select Pypy3
# # INPUT:
# 2
# 1 2
#--------Yashvi Bhadania--------