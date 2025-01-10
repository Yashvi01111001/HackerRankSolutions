from collections import OrderedDict
s = input()
letters_count = {}
for _ in s:
    # print(_)
    if _ not in letters_count:
        letters_count[_]=1
    else:
        letters_count[_]+=1  
    # print(letters_count)
    
# Sorting the items in descending order by value, then ascending order by key (alphabetically) e.g.(-item[1],item[0])
# lambda is a small anonymous function wihtout a name in Python
# Remember that each item is a tuple like (key, value). So, item[1] refers to the value part of the key-value pair (on which we're sorting).
sorted_items = sorted(letters_count.items(), key=lambda item: (-item[1],item[0]))
ordered_dict = OrderedDict(sorted_items)
# print(ordered_dict)

# Printing the top three entries:
count = 0
for key, value in ordered_dict.items():
    print(key, value)
    count += 1
    if count == 3:
        break

# # SAMPLE INPUT:
# aabbbccde

#--------Yashvi Bhadania--------
