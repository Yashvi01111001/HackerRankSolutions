n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
#input().split() reads a line of input, splits it into words based on whitespace, and returns a list of these words.
# The first word from the list is assigned to the variable 'name'.
# All remaining words from the list are captured into the variable 
#'line' using *line.
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()


# # To display the contents of the student_marks dictionary:
# for name, scores in student_marks.items():
#     print(name, scores)

for name, scores in student_marks.items():
    if name == query_name:
        # print(name)
        avg_score = sum(scores)/len(scores)
        # print(avg_score)
        formatted_score = format(avg_score, ".2f")
        print(formatted_score)



# # INPUT:
# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh

#--------Yashvi Bhadania--------