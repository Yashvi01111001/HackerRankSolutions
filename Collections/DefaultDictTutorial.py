# Enter your code here. Read input from STDIN. Print output to STDOUT
# Default value is 0

from collections import defaultdict

n, m = map(int, input().split())
list1=[]
list2=[]
for _ in range(n):
    list1.append(input())
for _ in range(m):
    list2.append(input())
    
# print(list1)
# print(list2)

letter_positions = defaultdict(list)

for i, letter in enumerate(list1):  # Iterate with index
    letter_positions[letter].append(i + 1)  # Store 1-indexed positions
# print(letter_positions)
for search_letter in list2:
    if search_letter in letter_positions:
        # Printing positions space-separated:
        print(*letter_positions[search_letter])  
    else:
        print(-1)  # Print -1 if no match is found

# # SAMPLE INPUT:
# 5 2 
# a 
# a
# b
# a
# b
# a 
# b

#--------Yashvi Bhadania--------