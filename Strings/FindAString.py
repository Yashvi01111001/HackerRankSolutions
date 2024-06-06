def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        # print(string[i])
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
            
    
    return count

#.strip() is an in-built method that removes leading and trailing whitespace (spaces, tabs, newlines) from a string. 
#It does not remove whitespace within the string, only from the beginning and end.

# if __name__ == '__main__':
string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

# # INPUT:
# ABCDCDC
# CDC

#--------Yashvi Bhadania--------