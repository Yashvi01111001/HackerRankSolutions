#SRC: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

#MY PROGRAM ON HACKERRANK:
def split_and_join(line):
    # write your code here
    #Convert the string into a list of strings
    line = line.split(" ") #the string is split based on a delimeter (in this case the space between words)
    # print(line)
    #Next, convert the list of strings into a string with delimeter (-)
    line = "-".join(line)
    return line
# if __name__ == '__main__':
line = input()
result = split_and_join(line)
print(result)

# # INPUT:
# this is a string   

#--------Yashvi Bhadania--------