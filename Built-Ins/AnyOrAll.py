# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
integers_list = list(map(int, input().split()))
print(all(i>0 for i in integers_list) and any(str(i) == str(i)[::-1] for i in integers_list))

# # SAMPLE INPUT:
# 5
# 12 9 61 5 14 
#--------Yashvi Bhadania--------
