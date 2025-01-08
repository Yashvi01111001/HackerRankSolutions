# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

word_counts = OrderedDict()
for _ in range(n):
    words = input()
    
    if words not in word_counts:
        word_counts[words] = 0 # Initialize count to 0 for new words
    word_counts[words]+=1 # Increment count for existing or new words
# PRINTING THE RESULTS:   
print(len(word_counts)) 
for results in word_counts:
    print(word_counts[results], end=" ")

# # SAMPLE INPUT:
# 4
# bcdef
# abcdefg
# bcde
# bcdef

#--------Yashvi Bhadania--------
