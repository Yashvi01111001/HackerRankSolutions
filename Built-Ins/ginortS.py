# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

lowercase = ''.join(sorted(c for c in s if c.islower()))
uppercase = ''.join(sorted(c for c in s if c.isupper()))
odd_digits = ''.join(sorted(str(d) for d in [int(c) for c in s if c.isdigit() and int(c) % 2 != 0]))
even_digits = ''.join(sorted(str(d) for d in [int(c) for c in s if c.isdigit() and int(c) % 2 == 0]))

print(lowercase+uppercase+odd_digits+even_digits)

# # SAMPLE INPUT:
# Sorting1234

#--------Yashvi Bhadania--------
