# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
columns = input().split()
# print(columns)
entries = []
total_sum = 0
valid_count = 0

for _ in range(N):
    # Spliting the input line into a list of strings:
    entry = input().split()
    entries.append(entry)
# print(entries)

# Finding the index of the "MARKS" column since columns can be in any order:
marks_index = columns.index("MARKS")  

for entry in entries:
    element_containing_marks = int(entry[marks_index])
    total_sum += element_containing_marks
    valid_count += 1

if valid_count > 0:
    average = total_sum / valid_count
    print("{:.2f}".format(average))  # Format to 2 decimal places

# # SAMPLE INPUT:
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6

#--------Yashvi Bhadania--------