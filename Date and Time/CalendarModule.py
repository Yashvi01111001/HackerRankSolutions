# SRC: https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
# print(calendar.TextCalendar(firstweekday=7).formatyear(2024))

# Split the input into day, month, and year
# day, month, year = map(int, input().split())
month, day, year = map(int, input().split())

# Get the weekday (0 = Monday, ..., 6 = Sunday)
weekday_index = calendar.weekday(year, month, day)

# Map weekday index to day name
day_name = calendar.day_name[weekday_index].upper()

print(day_name)


# # SAMPLE INPUT:
# 08 05 2015

#--------Yashvi Bhadania--------