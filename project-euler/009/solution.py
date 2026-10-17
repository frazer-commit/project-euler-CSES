import math

"""
Eucild's Formula solution.
"""

def find_half_sqrt_factors(n):
    target = n // 2
    factor = int(math.sqrt(target))
    
    found = False

    while not found:
        if n % factor == 0:
            found = True
        else:
            factor -= 1

    return (target // factor, factor)


def solve():
    n = 1000

    pair = find_half_sqrt_factors(n)
    
    n = pair[0] - pair[1]
    m = pair[1]

    prod = 2 * m * n * (m**4 - n**4)

    print(prod)

if __name__ == "__main__":
    solve()
