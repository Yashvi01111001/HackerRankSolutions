# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
my_set_a = set(map(int, input().split()))
N = int(input())
my_set_b = set(map(int, input().split()))


s_diff_a = my_set_a.difference(my_set_b)
# print(s_diff_a)
my_list_a = list(s_diff_a)
# print(my_list_a)

    
s_diff_b = my_set_b.difference(my_set_a)
my_list_b = list(s_diff_b)

result = []
for i in s_diff_a:
    result.append(i)
for i in s_diff_b:
    result.append(i)
result.sort()
# print(result)

for i in result:
    print(i)

# # INPUT:
# 4           
# 2 4 5 9     
# 4           
# 2 4 11 12

#--------Yashvi Bhadania--------