my_nested_list = []
scores_list = []
n = 0
for _ in range(int(input())):
    name = input()
    score = float(input())
        
    my_nested_list.append([name, score])
    n += 1
    scores_list.append(score)
min_score = min(scores_list)
# print(min_score)

new_scores_list = []
while n>1:
    for i in scores_list:
        if i != min_score:
            new_scores_list.append(i)
        n -= 1   
        
    if new_scores_list:
        second_min_score = min(new_scores_list)  
        # print(second_min_score)
            
#Next, print names of 2nd min score scorers
second_min_scorers = []
for student in my_nested_list:
    if student[1] == second_min_score: #using index 1 bcos we stored name at index 0 and score at index 1, thus we are accessing score
        second_min_scorers.append(student[0])
second_min_scorers.sort()
# print(second_min_scorers)
for name in second_min_scorers:
    print(name)
        
# #Short-hand for above:
# second_min_scorers = [student[0] for student in my_nested_list if student[1] == second_min_score]
# for name in second_min_scorers:
#     print(name)
        
# # INPUT:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

#--------Yashvi Bhadania--------
