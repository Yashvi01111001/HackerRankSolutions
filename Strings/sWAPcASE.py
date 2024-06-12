def swap_case(s):
    swapped_chars = []
    for _ in s:
        if _.islower():
            swapped_chars.append(_.upper())
        elif _.isupper():
            swapped_chars.append(_.lower())
    
    #the join() method is called on an empty string (''), and the list of characters (swapped_chars) is passed as an 
    #argument. This method concatenates each element of the list into a single string, with the empty string acting as 
    #a separator. Since we want to concatenate the characters without any separator between them, we use an empty string.
        else:
            swapped_chars.append(_)  # Keep characters unchanged if not at specified indexes
    #the join() method below is called on an empty string (''), and the list of characters (swapped_chars) is passed as an 
    #argument. This method concatenates each element of the list into a single string, with the empty string acting 
    #as a separator. Since we want to concatenate the characters without any separator between them, we use 
    #an empty string:    
    swapped_chars = ''.join(swapped_chars)
            
    return swapped_chars

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# # INPUT:
# HackerRank.com presents "Pythonist 2".

#--------Yashvi Bhadania--------