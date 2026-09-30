"""
This is optimised using the cool 11 is a factor
trick.

Also optimised such that it doesn't check
the same pairs twice by using:

for b in range(999, 100, -1)
"""

def check_palindrome(n):
    old_n = n
    flipped = 0

    while n != 0:
        flipped += n % 10
        flipped *= 10
        n //= 10

    flipped //= 10

    return flipped == old_n

def solve():
    largest = 0
    for a in range(990, 100, -11):
        if a * 999 < largest:
            break

        for b in range(999, a - 1, -1):
            product = a * b

            if product < largest:
                break
            
            if check_palindrome(product):
                largest = product

    print(largest)

if __name__ == "__main__":
    solve()
