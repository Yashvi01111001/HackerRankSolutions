for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i // 9) ** 2)

# NOTE: Remove this line and the rest below it for the editor to accept your minimum two lines of code

# Not your normal Math logic:
# The squares of the numbers of the form 1, 11, 111, 1111, 11111,... are the palindrome numbers!!!

# The above print line basically does this:
# 1st Iteration: 10//9 is 1 (since // is floor division, it rounds down to the floor number), then 1^(2) is 1
# 2nd Iteration: 100//9 is 11, then 11^(2) is 121
# 3rd Iteration: 1000//9 is 111, then 111^(2) is 12321
# 4th Iteration: 10000//9 is 1111, then 1111^(2) is 1234321
# 5th Iteration: 100000//9 is 11111, then 11111^(2) is 123454321

# # SAMPLE INPUT:
# 5

#--------Yashvi Bhadania--------