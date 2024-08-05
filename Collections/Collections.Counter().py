# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
available_sizes = list(map(int, input().split()))
N = int(input())
desired_sizes = [list(map(int, input().split())) for _ in range(N)]

available_sizes_cntr = Counter(available_sizes).items()

money = 0
for size, price in desired_sizes:
    if size in available_sizes:
        money += price
        available_sizes.remove(size)
        # print(available_sizes)
print(money)


# # SAMPLE INPUT:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

#--------Yashvi Bhadania--------