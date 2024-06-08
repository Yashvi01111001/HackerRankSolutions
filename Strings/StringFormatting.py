def print_formatted(number):
    print(hex(900))
    # your code goes here
    # Calculating the width of the binary representation of the largest number:
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        # binary_num = bin(i)[2:]
        # # space = len(binary_num)
        decimal_num = i
        octal_num = oct(i)[2:]
        hexadecimal_num = hex(i)[2:].upper()
        binary_num = bin(i)[2:]
        
        # Print each number with appropriate spacing
        print("{:>{width}} {:>{width}} {:>{width}} {:>{width}}".format(decimal_num, octal_num, hexadecimal_num, binary_num, width=width))
        
# {}: This is a placeholder for the value that will be inserted during formatting.
# >: This indicates that the value should be right-aligned within the specified width.
# {width}: This is a placeholder for the width parameter, which will be replaced with the actual width value during formatting.
# So, {:>{width}} specifies that the value should be right-aligned within the specified width.

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    
# # INPUT:
# 17 

#--------Yashvi Bhadania--------