# Enter your code here. Read input from STDIN. Print output to STDOUT
# Convert Input Data Type from STR to INT
# NM = input()
# # print(type(NM))
# # # for _ in range(NM):
# # #     N, M = input().split()
# # #     print(_)

# # Split the input string into a list of substrings
# split_NM = NM.split()

# # Convert each substring to an integer
# N = int(split_NM[0])
# M = int(split_NM[1])

# Easier way to convert it:
N, M = map(int, input().split())
# print(M)

stick = '|'
dot = '.'
hyphen = '-'

#TOP PART (1 of 3)
for i in range((N-1)//2):
    pattern = ((dot+stick+dot)*i)+dot+stick+dot+((dot+stick+dot)*i)
    padded_pattern = pattern.rjust((M - len(pattern))//2 + len(pattern), hyphen).ljust(M, hyphen)
    print(padded_pattern)


#MIDDLE PART (2 of 3)

print("WELCOME".center(M, '-'))

    
#BOTTOM PART (3 of 3)
for i in range((N-1)//2):
    pattern = ((dot+stick+dot)*((N-1)//2-i-1))+dot+stick+dot+((dot+stick+dot)*((N-1)//2-i-1))
    padded_pattern = pattern.rjust((M - len(pattern))//2 + len(pattern), hyphen).ljust(M, hyphen)
    print(padded_pattern)

# # INPUT:
# 9 27

#--------Yashvi Bhadania--------