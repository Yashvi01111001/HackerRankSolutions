# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

and_pattern = r'(?<= )&&(?= )'
or_pattern = r'(?<= )\|\|(?= )'

for _ in range(n):
    line = input()
    line = re.sub(and_pattern, 'and', line)
    line = re.sub(or_pattern, 'or', line)
    print(line)

# # SAMPLE INPUT:
# 11
# a = 1;
# b = input();

# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.

#--------Yashvi Bhadania--------