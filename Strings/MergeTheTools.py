def merge_the_tools(string, k):
    # your code goes here
    group = []
    for i in range(0, len(string), k):
        group.append(string[i:i+k])
    # print(group)
    
    for sub_groups in group:
        # Convert the string to a set to automatically remove duplicates
        unique_chars_list = []
        for char in sub_groups:
            # print(char)
            if char not in unique_chars_list:
                unique_chars_list.append(char)
        result = ''.join(unique_chars_list)
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# # INPUT:
# AABCAAADA
# 3  

#--------Yashvi Bhadania--------