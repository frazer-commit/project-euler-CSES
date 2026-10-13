import math

"""
I like this more.
"""

def solve(digits = 1000):
    sqrt5 = math.sqrt(5)

    PHI = (1 + sqrt5) / 2
    inv_log2_PHI = 1 / math.log2(PHI)

    PHI_10 = math.log2(10) * inv_log2_PHI
    PHI_sqrt5 = math.log2(sqrt5) * inv_log2_PHI

    index = PHI_10 * (digits - 1) + PHI_sqrt5
    index = math.ceil(index)

    print(index)

if __name__ == "__main__":
    solve() # This solves the thing
