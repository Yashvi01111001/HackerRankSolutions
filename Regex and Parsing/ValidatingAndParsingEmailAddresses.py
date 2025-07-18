# # Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

pattern = re.compile(r'^[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

N = int(input())
for _ in range(N):
    address = input()
    name, email_addr = email.utils.parseaddr(address)
    if pattern.match(email_addr):
        print(f"{name} <{email_addr}>")

# # SAMPLE INPUT:
# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>

#--------Yashvi Bhadania--------