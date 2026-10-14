from decimal import Decimal

"""
This solution is really boring and I'll
make a better one.
"""

def solve()
    nums = set()

    for a in range(2, 101):
        for b in range(2, 101):
            nums.add(Decimal(a)**b)

    print(len(nums))


if __name__ == "__main__":
    solve()
