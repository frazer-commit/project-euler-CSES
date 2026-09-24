"""
This solution is bruteforce and I hate it.
"""

import time

def check_palindrome(n1):
    oldn1 = n1
    n2 = 0

    while n1 != 0:
        n2 += (n1 % 10)
        n2 *= 10
        n1 //= 10
    
    n2 /= 10
    
    return oldn1 == n2

def solve():
    found = False
    
    largest = [0, 0, 0]

    for n1 in range(999, 0, -1):
        for n2 in range(999, 0, -1):
            product = n1 * n2
            found = check_palindrome(product)
            if found and product > largest[2]:
                largest = [n1, n2, product]
    print(largest)

if __name__ == "__main__":
    solve()
