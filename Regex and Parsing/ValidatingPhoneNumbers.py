# # Enter your code here. Read input from STDIN. Print output to STDOUT
# N = int(input())
# for i in range(N):
#     number = str(input().strip())
#     # print(number)
#     list = [7,8,9]
#     if len(number)==10 and int(number[0]) in list and number.isdigit():
#         print("YES")
#     else:
#         print("NO")

import re
N = int(input())
pattern = re.compile(r'^[789]\d{9}$')
for _ in range(N):
    number = input().strip()
    if pattern.fullmatch(number):
        print("YES")
    else:
        print("NO")

# # SAMPLE INPUT:
# 2
# 9587456281
# 1252478965

#--------Yashvi Bhadania--------