#SRC: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    # your code goes here
    array = set(array)
    result_my = sum(array)/len(array)
    return result_my
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



# # INPUT:
# 10
# 161 182 161 154 176 170 167 171 170 174

#--------Yashvi Bhadania--------
