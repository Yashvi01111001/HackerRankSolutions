n = int(input())
arr = map(int, input().split())
my_list = list(arr)
arr = my_list

max_score = max(arr)

new_arr = []

while n>1:
    for score in arr:
        if score != max_score:
            new_arr.append(score)
        n -= 1   
    # print(new_arr)
    if new_arr:
        second_max_score = max(new_arr)  
        print(second_max_score)
    else:
        pass

# # INPUT:
# 5
# 2 3 6 6 5

#--------Yashvi Bhadania--------