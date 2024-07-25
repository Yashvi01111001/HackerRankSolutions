for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * (10 ** i) // 9) 

# NOTE: Remove this line and the rest below it for the editor to accept your minimum two lines of code

# (since // is floor division, it rounds down to the floor number)
# You make use of the fact that 10 // 9 is 1, 100 // 9 is 11, 1000 // 9 is 111, etc.; 
# get yourself enough zeros to produce the right number of digits, and multiply the repeating 1 number 
# with i to get a number of repeated i digits.

# # SAMPLE INPUT:
# 5

#--------Yashvi Bhadania--------