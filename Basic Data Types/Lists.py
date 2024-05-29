N = int(input())
command_values = []
result = []
for _ in range(N):
    command, *line = input().split()
#input().split() reads a line of input, splits it into words based on whitespace, and returns a list of these words.
# The first word from the list is assigned to the variable 'command'.
# All remaining words from the list are captured into the variable 'line' using *line.
    
    input_nums = list(map(int, line))
    # print(input_nums)
    command_values.append([command, input_nums])
# print(command_values)
for command, input_nums in command_values:
    if command == "insert":
        # print("Found an insert command.")
        idx = input_nums[0] #getting the index position specified by user input
        insert_value = input_nums[1] #getting the value through user input
        result.insert(idx,insert_value) #inserting value 'insert_value' at index position 'idx'
    
    elif command == "print":
        print(result)

    elif command == "remove":
        result.remove(input_nums[0])
        
    elif command == "append":
        result.append(input_nums[0])
        
    elif command == "sort":
        result.sort()
        
    elif command == "pop":
        result.pop()
        
    elif command == "reverse":
        result.reverse()
        
    else:
        pass

# # INPUT:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

#--------Yashvi Bhadania--------