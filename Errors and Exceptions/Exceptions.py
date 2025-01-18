# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    a, b = input().split()
    # print(a,b)
    try:
        a = int(a)
        b = int(b)
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

# # SAMPLE INPUT:
# 3
# 1 0
# 2 $
# 3 1

#--------Yashvi Bhadania--------
