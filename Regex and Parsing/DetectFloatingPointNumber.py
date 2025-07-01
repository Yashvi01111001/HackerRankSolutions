import re

pattern = r'^[+-]?(\d+\.\d+|\.\d+)$'

T = int(input())

for N in range(T):
    # print(input())
    strings = input().strip()
    
    if re.match(pattern, strings):
        try:
            float(strings)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)

# # SAMPLE INPUT:
# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

#--------Yashvi Bhadania--------