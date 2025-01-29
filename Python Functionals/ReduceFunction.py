from fractions import Fraction
from functools import reduce

def product(fracs):
    # Base Case (Important Clarification): The original code had a flawed base case:
    if len(fracs) == 1:
        return fracs[0].numerator, fracs[0].denominator
    # This is not necessary and creates an inconsistency. reduce works perfectly well with a single element. Removing this base case makes the code cleaner and correct.
    else:
        # The reduce function applies this lambda function cumulatively to the fracs list. For example, if fracs is [1/2, 2/3, 3/4], reduce will do the following:
        # (1/2) * (2/3) = 1/3
        # (1/3) * (3/4) = 1/4 The final result 1/4 is returned.
        t = reduce( lambda x, y : x * y, fracs )
        return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
  
# # SAMPLE INPUT:
# 3
# 1 2
# 3 4
# 10 6

#--------Yashvi Bhadania--------
