# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            name = attr[0]
            value = attr[1] if attr[1] is not None else "None"
            print(f"-> {name} > {value}")
    
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            name = attr[0]
            value = attr[1] if attr[1] is not None else "None"
            print(f"-> {name} > {value}")

n = int(input())
html = ""
for _ in range(n):
    html += input()

parser = MyHTMLParser()
parser.feed(html)

# # SAMPLE INPUT:
# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>  

#--------Yashvi Bhadania--------