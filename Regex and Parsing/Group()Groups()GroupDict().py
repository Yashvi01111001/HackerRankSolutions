import re

# Read input
s = input()

# Regular expression pattern to find the first alphanumeric character that repeats consecutively
match = re.search(r'([a-zA-Z0-9])\1', s)

# Print result
if match:
    print(match.group(1))
else:
    print(-1)

# # SAMPLE INPUT:
# ..12345678910111213141516171820212223

#--------Yashvi Bhadania--------