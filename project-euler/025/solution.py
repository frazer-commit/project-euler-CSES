import math
from decimal import Decimal

def solve():
    digits = 1000

    PHI = Decimal((1 + math.sqrt(5)) / 2)

    big = Decimal(10)**(digits - 1)
    big *= Decimal(math.sqrt(5))

    x = big.ln() / PHI.ln()
    x = math.ceil(x)

    print(x)
    

if __name__ == "__main__":
    solve()
