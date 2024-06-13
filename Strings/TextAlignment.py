thickness = int(input()) #This must be an odd number
# thickness = 5
c = 'H'

#Top Cone
for i in range(thickness): #it will print thickness lines of output
    print((c*i).rjust(thickness)+c+(c*i).ljust(thickness))

#Top Pillars
for i in range(thickness+1): #prints thickness + 1 lines, i.e. 5+1 lines in total
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2): #bcos num of lines is 3 not 5
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# # INPUT:
# 5

#--------Yashvi Bhadania--------