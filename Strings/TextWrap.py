import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    result = '\n'.join(result)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

    
# # INPUT:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

#--------Yashvi Bhadania--------