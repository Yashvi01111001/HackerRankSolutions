n = int(input())
s = set(map(int, input().split()))

N = int(input())
# command, *number = [input().split() for i in range(N)]
for i in range(N):
    command, *number = input().split()
    number = list(map(int, number))

    if command=="pop":
        s.pop()
    if command=="remove":
        s.remove(number[0])
    if command=="discard":
        s.discard(number[0])

result = sum(s)
print(result)


# # INPUT:
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

#--------Yashvi Bhadania--------