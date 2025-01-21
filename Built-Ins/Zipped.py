# Enter your code here. Read input from STDIN. Print output to STDOUT

# N (students), X (subjects)
N, X = map(int, input().split())
grade_all_subjects=[]
for _ in range (X):
    grades = list(map(float, input().split()))
    # print(grades)
    grade_all_subjects.append(grades)
    
# Transpose list of lists to get grades by student
grades_by_student = list(zip(*grade_all_subjects))
# print(grades_by_student)

for _ in grades_by_student:
    sum=0
    cnt=0
    # print(list(_))
    for x in _:
        sum+=x
        cnt+=1
    print(sum/cnt)

# # SAMPLE INPUT:
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5
#--------Yashvi Bhadania--------