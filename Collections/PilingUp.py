# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    side_lengths = deque(map(int, input().split()))
    # print(*side_lengths)
    pile = []
    
    while side_lengths:
        
        # Check which end of the deque has the larger side length (left or rightmost):
        if side_lengths[0] <= side_lengths[-1]:
            # Removing rightmost cube and adding to pile list
            pile.append(side_lengths.pop())
            
        else:
            # Removing leftmost cube and adding to pile list
            pile.append(side_lengths.popleft())
    
    # Creating a new list that is a sorted (descending) copy of pile:   
    if pile == sorted(pile, reverse=True):
        print("Yes")
    else:
        print("No")
            
# # SAMPLE INPUT:
# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
#--------Yashvi Bhadania--------
