def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    vowels = ["A","E","I","O","U"]
    
    for start_index in range(length):
        score = length - start_index
        if string[start_index] in vowels:
            kevin_score += score
        else:
            stuart_score += score
    
    if stuart_score ==  kevin_score:
        print("Draw")
    if stuart_score>kevin_score:
        print("Stuart", stuart_score)
    if kevin_score>stuart_score:
        print("Kevin", kevin_score)
        

if __name__ == '__main__':
    s = input()
    minion_game(s)

    
# # INPUT:
# BANANA

#--------Yashvi Bhadania--------