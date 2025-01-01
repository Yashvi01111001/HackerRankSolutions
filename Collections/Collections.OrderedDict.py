# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
item_counts={}
for _ in range(N):
    # Split from the right to handle spaces in item name:
    # the 1 is the maxsplit argument for the rsplit() method. It determines the maximum number of splits that will be performed, starting from the right side of the string.
    # rsplit(separator, maxsplit)
    item_name, price = input().rsplit(" ", 1)
    price = int(price)
    # print(item_name)
    # print(price)
    if item_name not in item_counts:
        item_counts[item_name] = 0
    item_counts[item_name]+=price
    
# print(item_counts)
#  .items() is used to iterate through the key-value pairs of a dictionary, it returns a view object that yields a sequence of key-value pairs as tuples.
for item, total_price in item_counts.items():
    print(item, total_price)

# # SAMPLE INPUT:
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

#--------Yashvi Bhadania--------
