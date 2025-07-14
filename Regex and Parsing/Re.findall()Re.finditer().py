# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

# Regex explanation:
# - (?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]) - positive lookbehind for a consonant
# - ([aeiouAEIOU]{2,}) - group of 2 or more vowels
# - (?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]) - positive lookahead for a consonant
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)

# # SAMPLE INPUT:
# rabcdeefgyYhFjkIoomnpOeorteeeeet

#--------Yashvi Bhadania--------