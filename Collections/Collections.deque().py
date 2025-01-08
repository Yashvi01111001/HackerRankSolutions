# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

N = int(input())
my_deque = deque()

for _ in range(N):
    # methods, values = input().split
    # Split the line into a list of parts:
    line = input().split()
    # The first part is always the method:
    method = line[0]
    
    if method == "append":
        my_deque.append(line[1])
    if method == "appendleft":
        my_deque.appendleft(line[1])
    if method == "pop":
        my_deque.pop()
    if method == "popleft":
        my_deque.popleft()
        
print(*my_deque)  
# The asterisk (*), when used before an iterable (like a list, tuple, or deque) in a function call, performs unpacking. It takes the elements of the iterable and passes them to the function as separate arguments.

# # SAMPLE INPUT:
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

#--------Yashvi Bhadania--------
