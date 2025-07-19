import re

n = int(input())
inside_block = False
pattern = re.compile(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b')

for _ in range(n):
    line = input()

    if inside_block:
        matches = pattern.findall(line)
        for match in matches:
            print(match)

    # Now update block status AFTER processing line
    if '{' in line:
        inside_block = True
    if '}' in line:
        inside_block = False

# # SAMPLE INPUT:
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }   

#--------Yashvi Bhadania--------