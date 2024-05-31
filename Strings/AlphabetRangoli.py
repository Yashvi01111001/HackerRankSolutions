def print_rangoli(size):
    
    import string
    
    #FIRST TOP LINE
    if size!=1:
        print(string.ascii_letters[size-1].center(size+(size-1)+(size+(size-1)-1), '-'))
    else:
        pass
    
    #TOP LINES
    last = size-1
    second_last = size-2
    for i in range(size-2):
        line_chars2 = '-'.join(string.ascii_letters[last:size])
    
        line_chars1 = '-'.join(string.ascii_letters[second_last:size])[::-1] #to reverse the string for the left side
    
        line = '-'+line_chars1+'-'+line_chars2+'-'
        print(line.center(size+(size-1)+(size+(size-1)-1), '-'))
        last -= 1
        second_last -= 1
            
            
    #CENTER LINE
    if size!=1:
        middle_line_chars2 = '-'.join(string.ascii_letters[:size])
    
        middle_line_chars1 = '-'.join(string.ascii_letters[1:size])[::-1]
    
        middle_line = middle_line_chars1+'-'+middle_line_chars2
        print(middle_line)
    else:
        middle_line = string.ascii_letters[0]
        print(middle_line)

    #BOTTOM LINES
    first = 1
    second = 2
    for i in range(size-2):
        line_chars2 = '-'.join(string.ascii_letters[first:size])
    
        line_chars1 = '-'.join(string.ascii_letters[second:size])[::-1] #to reverse the string for the left side
    
        line = '-'+line_chars1+'-'+line_chars2+'-'

        print(line.center(size+(size-1)+(size+(size-1)-1), '-'))

        first += 1
        second += 1
            
    #LAST BOTTOM LINE
    if size!=1:
        print(string.ascii_letters[size-1].center(size+(size-1)+(size+(size-1)-1), '-'))
    else:
        pass

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# # INPUT:
# 5

#--------Yashvi Bhadania--------