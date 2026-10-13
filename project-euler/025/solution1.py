import math
from decimal import Decimal

"""
I like this. Because its simple and
elegant.
"""

def solve():
    digits = 1000

    PHI = Decimal((1 + math.sqrt(5)) / 2)

    big = Decimal(10)**(digits - 1)
    big *= Decimal(math.sqrt(5))

    index = big.ln() / PHI.ln()
    index = math.ceil(index)

    print(index)

if __name__ == "__main__":
    solve() # This solves the thing
