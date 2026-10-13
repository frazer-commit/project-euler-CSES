"""
I like this solution
"""

def solve():
    size = 1001

    s = size // 2
    total = 0

    total += (4 * s * (s+1) * (2*s + 1)) // 6
    total += (s * (s+1)) // 2
    total += s

    total *= 4
    total += 1  # The 1 in the center

    print(total)

if __name__ == "__main__":
    solve()
